# - Author: Ad_Astra - #

from pathlib import Path   
from logzero import logger, logfile 
from sense_hat import SenseHat  
from picamera import PiCamera   
from orbit import ISS  
from time import sleep
from datetime import datetime, timedelta 
from PIL import Image
from pycoral.adapters import common
from pycoral.adapters import classify
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.dataset import read_label_file

import csv
import exif
import math
import cv2
import numpy as np
import os, sys

#Special value of speed 
NO_SPEED = 9999.99

sense = SenseHat()
sense.set_imu_config(True, True, True)  

def f_get_magnetometer():
    magnetic = sense.get_compass_raw()
    return magnetic['x'], magnetic['y'], magnetic['z']

def f_get_gyroscope():
    gyro_only = sense.get_gyroscope()
    return gyro_only['pitch'], gyro_only['roll'], gyro_only['yaw']

def f_get_accelerometer():
    acceleration = sense.get_accelerometer_raw()
    return acceleration['x'], acceleration['y'], acceleration['z']

def create_csv_file(data_file, bool = True):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:  
        writer = csv.writer(f)
        if bool:  
            header = ("Counter", "Date/time", "Latitude", "Longitude", "Accelerometer_x", "Accelerometer_y", "Accelerometer_z", "Gyroscope_pitch", "Gyroscope_roll", "Gyroscope_yaw", "Magnetometer_x", "Magnetometer_y", "Magnetometer_z")
        else:
            header = ("Counter","ML", "Speed")
        writer.writerow(header) 

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def convert(angle):
    """
    Convert a `skyfield` Angle to an EXIF-appropriate
    representation (rationals)
    e.g. 98° 34' 58.7 to "98/1,34/1,587/10"

    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    sign, degrees, minutes, seconds = angle.signed_dms() 
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    location = ISS.coordinates()

    # Convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(location.latitude)       
    west, exif_longitude = convert(location.longitude)

    # Set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude             
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"
    
    # Capture the image
    camera.capture(image) 

"""
ISS SPEED
"""
def get_time(image):
    with open(image, 'rb') as image_file:
        img = exif.Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time


def get_time_difference(image_1, image_2):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    time_difference = time_2 - time_1
    return time_difference.seconds

def convert_to_cv(image_1, image_2):
    image_1_cv = cv2.imread(image_1, 0)
    image_2_cv = cv2.imread(image_2, 0)
    return image_1_cv, image_2_cv

def calculate_features(image_1, image_2, feature_number):
    orb = cv2.ORB_create(nfeatures = feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2, None)
    return keypoints_1, keypoints_2, descriptors_1, descriptors_2

def calculate_matches(descriptors_1, descriptors_2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):
    match_img = cv2.drawMatches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches[:100], None)
    resize = cv2.resize(match_img, (1600,600), interpolation = cv2.INTER_AREA)
    cv2.imshow('matches', resize)
    cv2.waitKey(0)
    cv2.destroyWindow('matches')

def find_matching_coordinates(keypoints_1, keypoints_2, matches):
    coordinates_1 = []
    coordinates_2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = keypoints_1[image_1_idx].pt
        (x2,y2) = keypoints_2[image_2_idx].pt
        coordinates_1.append((x1,y1))
        coordinates_2.append((x2,y2))
    return coordinates_1, coordinates_2

def calculate_mean_distance(coordinates_1, coordinates_2):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
        distance = math.hypot(x_difference, y_difference)
        all_distances = all_distances + distance

    # In case of calculating keyponts error as merged_coordinates = 0, return 0 in order to obtain special value of 9999.99
    if len(merged_coordinates) == 0:
        return 0
    else:
        return all_distances / len(merged_coordinates)                                    

def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
    distance = feature_distance * GSD / 100000
    speed = distance / time_difference

    # If feature_distance is equals to 0, speed is also 0. So if speed is 0 we return NO_SPEED (9999.99)
    if speed == 0:
        return NO_SPEED
    else:
        return speed

def main():
    #Saving folder path
    base_folder = Path(__file__).parent.resolve()  

    # Set a logfile name
    logfile(base_folder/"events.log") 

    # Set up Sense Hat
    sense = SenseHat()

    # Set up camera
    cam = PiCamera() 
    cam.resolution = (1296, 972)  

    # Initialise the CSV file with sensors value
    data_file = base_folder/"data.csv"
    create_csv_file(data_file)

    # Initialise the CSV file with ML and speed value
    speed_file = base_folder/"speed.csv"
    create_csv_file(speed_file, bool = False)

    # Initialise the photo counter
    counter = 1

    # Record the start and current time
    start_time = datetime.now()
    now_time = datetime.now()

    #Machine Learning
    model_file = base_folder/'models/model_edgetpu.tflite' 
    label_night_file = base_folder/'models/labels.txt' 

    interpreter = make_interpreter(f"{model_file}")
    interpreter.allocate_tensors()

    size = common.input_size(interpreter)

    #Stack with previus image
    save_image = []

    result_ML = None

    while (now_time < start_time + timedelta(minutes = 180)):
        try:
            # Get coordinates of location on Earth below the ISS
            location = ISS.coordinates()

            # Save the current time 
            time = datetime.now()

            # Saving of sensors's values 
            accelerometer_x, accelerometer_y, accelerometer_z = f_get_accelerometer() 
            gyroscope_pitch, gyroscope_roll, gyroscope_yaw = f_get_gyroscope()
            magnetometer_x, magnetometer_y, magnetometer_z = f_get_magnetometer()

             # Tuple with sensor's values
            data = (
                counter,
                time,
                location.latitude.degrees,
                location.longitude.degrees,
                accelerometer_x, accelerometer_y, accelerometer_z,
                gyroscope_pitch, gyroscope_roll, gyroscope_yaw,
                magnetometer_x, magnetometer_y, magnetometer_z,
                datetime.now() 
            )
            add_csv_data(data_file, data)

            # Capture image
            image_file = f"{base_folder}/photo_{counter:03d}.jpg"
            capture(cam, image_file)
            image = Image.open(image_file).convert('RGB').resize(size, Image.LANCZOS)
            
            # FIRST ITERATION: 
            # During the first iteration a previus image doesn't exist, so the first image is saved (append in the stack) 
            if (counter == 1):
                save_image.append(image_file)

            #Machine Learning 
            common.set_input(interpreter, image)
            interpreter.invoke()
            classes = classify.get_classes(interpreter, top_k=1)

            labels = read_label_file(label_night_file)
            
            result_ML = labels.get(classes[0].id)
            
            # ISS SPEED
            if (counter != 1):
                # SELECTING IMAGES:
                # First one: the previus image (pop in the stack)
                # Second one: the current image
                image_1, image_2 = save_image.pop(), image_file 
                
                # Saving current image in the stack
                save_image.append(image_file)

                time_difference = get_time_difference(image_1, image_2) #get time difference between images
                image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
                keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
                matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
                coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
                average_feature_distance = calculate_mean_distance(coordinates_1, coordinates_2)
                speed = calculate_speed_in_kmps(average_feature_distance, 12648, time_difference)

                
                
            else:
                #FIRST ITERATION:
                #Setting the speed value as 0
                speed = 0 

            # Night result with ML:
            # Setting speed as NO_SPEED (9999.99)
            if result_ML == "night":
                data_speed = (
                    counter,
                    result_ML,
                    NO_SPEED
                )
                
            else:
                data_speed = (
                    counter,
                    result_ML,
                    speed
                )
            
            add_csv_data(speed_file, data_speed) 

            # Update the current time
            now_time = datetime.now()

            logger.info(f"iteration {counter}")
            counter += 1
            sleep(5)

        except Exception as e:
            logger.error(f'{e.__class__.__name__}: {e}')
            
            # EXCEPTION CASE:
            # Saving speed as NO_SPEED (9999.99) in case of convert_to_cv error
            data_speed = (
                counter,
                result_ML,
                NO_SPEED
            )
            add_csv_data(speed_file, data_speed)

            # Updating counter
            counter += 1

if __name__ == "__main__":
    main()
