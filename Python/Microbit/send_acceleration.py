#eseguire sul microbit
from microbit import *
while True:
    a = accelerometer.get_values()
    print(a)
    sleep(100)