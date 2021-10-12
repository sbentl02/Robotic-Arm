#!/usr/bin/env/python3.7
import time, math, sys
import board, busio
import RPi.GPIO as GPIO
from surface_mapping import *
from adafruit_servokit import ServoKit
from motors import IK_Solve
from get_xy import get_xy, read_SVG
from svgpathtools import svg2paths2

if __name__ == "__main__":
    #Initialize servo communication
    kit = ServoKit(channels=16)

    #Initialize global state variables
    previous_time = 0
    isMoving = False
    hasZMesh = False
    z_offset = 90
    sample_z = False
    isWriting = False
    N = 20
    step_interval = 10 #time per motor move in ms
    prev_state = 0

    #Setup GPIO control
    LED_RED = 23
    LED_GREEN = 24
    MESH_PIN = 27
    DRAW_PIN = 17

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(MESH_PIN, GPIO.IN)
    GPIO.setup(DRAW_PIN, GPIO.IN)

    #Start communication with Lidar

    #Move servos to initial positions
    kit.servo[0].angle = 90
    kit.servo[1].angle = 60
    kit.servo[2].angle = 30
    kit.servo[3].angle = 90

    #Read in SVG file
    xy_coords = read_SVG("Examples/initials_JA.svg", 10)

    main()


def time_ms():
    return time.time_ns() / 1000000

def main():
    while True:
        try:
            current_time = time_ms()
            sample_z = GPIO.input(MESH_PIN)
            isWriting = GPIO.input(DRAW_PIN)

            if sample_z == True:
                GPIO.output(LED_RED, 1)
                z_data = sample_surface(N, (-100, 100), (10, 100))
                inter, coef = surface_approximation(N, z_data, (-100, 100), (10, 100))
                has_ZMesh = True
            else:
                GPIO.output(LED_RED, 0)

            if hasZMesh:
                GPIO.output(LED_GREEN, 1)
            else: GPIO.output(LED_GREEN, 0)


            if (isWriting == True) & (not isMoving):
                if current_time - previous_time >= step_interval: #Check to see if we have taken longer than the step interval
                    #Get current path step

                    # Get x,y coordinates for drawing
                    x,y,down = get_xy(xy_coords, i)

                    #Get Z given current z mesh status
                    if has_ZMesh:
                        z = fit_func((x, y), inter, coef)
                    else:
                        z = z_offset


                    previous_time = current_time

                    #Attempt IK Solving
                    try:
                        angles = IK_Solve(x, y, z)
                    except Exception as e:
                        print("Inverse Kinematics failed! Exception: ", e)

                    for ang in angles:
                        kit.servo[ang].angle = angles[ang]

                    if (down and not prev_state):
                        pendown(x, y, z)
                    elif (not down and prev_state):
                        penup(x, y, z)

                    previous_time += step_interval
        except KeyboardInterrupt:
            break
    return

def sample_z_point(x, y):
    angles = IK_Solve(x, y, 0)

    for ang in angles:
        kit.servo[ang].angle = angles[ang]

    time.sleep(0.5)


def pendown(x, y, z):
    prev_state = 1
    #Attempt IK Solving
    try:
        angles = IK_Solve(x, y, z-10)
    except Exception as e:
        print("Inverse Kinematics failed! Exception: ", e)
    for ang in angles:
        kit.servo[ang].angle = angles[ang]

def penup(x, y, z):
    prev_state = 0
    try:
        angles = IK_Solve(x, y, z+10)
    except Exception as e:
        print("Inverse Kinematics failed! Exception: ", e)
    for ang in angles:
        kit.servo[ang].angle = angles[ang]
