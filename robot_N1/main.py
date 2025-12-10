#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
telecommande = InfraredSensor(Port.S1)
m_left = Motor(Port.B)
m_right = Motor(Port.C)
robot = DriveBase(m_left, m_right, 56, 114)

# Write your program here.
ev3.speaker.beep()



lecture = True
while lecture == True :
    liste_boutons = telecommande.buttons(1)

    if liste_boutons != []:
        print(liste_boutons)
        elt_liste = liste_boutons.pop()
        if elt_liste == Button.BEACON:
            lecture = False        
        if elt_liste == Button.LEFT_UP:
            robot.drive(50, 0)
        if elt_liste == Button.LEFT_DOWN:
            robot.drive(-50, 0)
        if elt_liste == Button.RIGHT_DOWN:
            robot.drive(0, 50)
        if elt_liste == Button.RIGHT_UP:
            robot.drive(0, -50)
        
    wait(200)
    




