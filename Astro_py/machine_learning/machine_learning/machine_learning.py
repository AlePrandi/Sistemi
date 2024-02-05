#!/usr/local/bin/python
from cProfile import label
import os, sys

#importing external libraries
from pathlib import Path
from xml.dom import NO_MODIFICATION_ALLOWED_ERR
from logzero import logger, logfile
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

from PIL import Image
from pycoral.adapters import common
from pycoral.adapters import classify
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.dataset import read_label_file

#ndvi import libraries
import cv2
import numpy as np
from fastiecm import fastiecm
from time import sleep


#night-day-model
model_night_file = script_dir/'modelsNight/model_edgetpu.tflite' # name of model, path dalla cartella di questo file verso il modello
data_night_dir = script_dir
label_night_file = data_night_dir/'labelsNight.txt' # Name of your label file

interpreter_night = make_interpreter(f"{model_night_file}")
interpreter_night.allocate_tensors()

size = common.input_size(interpreter_night)

#control of the second model (night)
image = Image.open(image_file).convert('RGB').resize(size, Image.ANTIALIAS)     #image file dovrebbe essere nel main code quando acquisisce l'immagine

common.set_input(interpreter_night, image)
interpreter_night.invoke()
classes = classify.get_classes(interpreter_night, top_k=1)

labels = read_label_file(label_night_file)

z = labels.get(classes[0].id)