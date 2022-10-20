from djitellopy import *
import keyboard
# This code will allow flight controls via your computer keyboard.

# Create a new instance of the tello drone, then connect to it.
tello = Tello()
tello.connect()

# Information functions.
def getTemp():
    temp = tello.get_temperature()
    print('Temperature: ', temp, "°")
def getHeight():
    height = tello.get_height()
    print('Height: ', height, "cm")
def getBattery():
    battery = tello.get_battery()
    print('Battery: ', battery, "%")
def getPitch():
    pitch = tello.get_pitch()
    print('Pitch: ', pitch, "°")
def getYaw():
    yaw = tello.get_yaw()
    print('Yaw: ', yaw, "°")
def getSpeed():
    speedX = tello.get_speed_x()
    speedY = tello.get_speed_y()
    speedZ = tello.get_speed_z()

    print("Speed X: ", speedX)
    print("Speed Y: ", speedY)
    print("Speed Z: ", speedZ)
def setActive(boolean):
    active = boolean

active = True
isFlying = False


def flight():
    global isFlying

    # Takeoff and landing controls.
    if keyboard.is_pressed('1') and isFlying is False:
        isFlying = True
        tello.takeoff()
    elif keyboard.is_pressed('2') and isFlying is True:
        tello.land()
        isFlying = False
    elif keyboard.is_pressed('esc'):
        setActive(False)

    # Linear movement.
    if keyboard.is_pressed('w'):
        tello.move_forward(50)
    elif keyboard.is_pressed('a'):
        tello.move_left(50)
    elif keyboard.is_pressed('s'):
        tello.move_back(50)
    elif keyboard.is_pressed('d'):
        tello.move_right(50)

    # Rotational movement.
    if keyboard.is_pressed('q'):
        tello.rotate_counter_clockwise(30)
    elif keyboard.is_pressed('e'):
        tello.rotate_clockwise(30)

    # Height controls.
    if keyboard.is_pressed('r'):
        tello.move_up(30)
    elif keyboard.is_pressed('f'):
        tello.move_down(30)

    # Get current drone information.
    if keyboard.is_pressed('t'):
        getTemp()
    elif keyboard.is_pressed('h'):
        getHeight()
    elif keyboard.is_pressed('b'):
        getBattery()
    elif keyboard.is_pressed('p'):
        getPitch()
    elif keyboard.is_pressed('y'):
        getYaw()
    elif keyboard.is_pressed('k'):
        getSpeed()

getBattery()
getTemp()

while active:
    flight()

