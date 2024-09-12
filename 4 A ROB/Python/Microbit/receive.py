import numpy as np
import sys
import serial, time
import pygame as pg
import threading, queue
import time


#pygame config
width = 1300
height = 600
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
ball = pg.image.load("./intro_ball.gif")
ballrect = ball.get_rect()
ballrect.centerx = width//2 + 1
ballrect.centery = height//2 + 1


black = 0, 0, 0
dt = 1
gamma = 0.05
q = queue.Queue()

class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM11"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)


running = True
rm = Read_Microbit()
rm.start()
pg.init()
speed = [0, 0]
div = 300
while running:
    acc = q.get()
    speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/div
    speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/div
    q.task_done()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    pg.display.flip()
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
    
rm.terminate()
rm.join()
