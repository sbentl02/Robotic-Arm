import time, math
#from adafruit_servokit import ServoKit

#kit = ServoKit(channels=16)

#Inverse Kinematic Equations for 3-link planar arm
length1 = math.sqrt(6**2 + 4**2)
length2 = 4*math.sqrt(2)
length3 = 2

#Set end effector coordinates
x_e = 10
y_e = 10
phi_e = math.pi/2

#Find wrist coordinates
x_w = x_e - length3 * math.cos(phi_e)
y_w = y_e - length3 * math.sin(phi_e)
print(x_w, y_w)

#Woodward's method
c2 = (x_w**2 + y_w**2 - length1**2 - length2**2)/(2*length1*length2)
s2 = -math.sqrt(1-c2**2)
theta2 = math.atan2(s2, c2)
print(theta2)


alpha = math.atan2(y_w, x_w)

theta2 = math.pi - math.acos((length1**2 + length2**2 - x_w**2 - y_w**2)/(2*length1*length2))
print(theta2)
theta1 = alpha - math.acos((x_w**2 + y_w**2 + length1**2 - length2**2)/(2*length1*math.sqrt(x_w**2 + y_w**2)))
print(theta1)
theta3 = phi_e - theta1 - theta2
print(theta3)
# kit.servo[0].angle = 180
# kit.continuous_servo[1].throttle = 1
# time.sleep(1)
# kit.continuous_servo[1].throttle = -1
# time.sleep(1)
# kit.servo[0].angle = 0
# kit.continuous_servo[1].throttle = 0
