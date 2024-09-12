from picamera import PiCamera

cam = PiCamera()

cam.resolution = (4056, 3040)

cam.capture("image1.jpg")