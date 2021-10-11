#!/usr/bin/env/python3
import time
import sys
from surface_mapping import *


previous_time = 0
isMoving = False
hasZMesh = False
sample_z = False
isWriting = False
step_interval = 10 #time per motor move in ms

def time_ms():
    return time.time_ns() / 1000000


def main():
    while True:
        try:
            current_time = time_ms()
            if sample_z = True:
                sample_surface(20, (-100, 100), (-100, 100))

            if current_time - previous_time <= step_interval:
                #move motor
                x, y = path[t] 
                





        except KeyboardInterrupt:
            break
    return



if __name__ == "__main__":
    main()



