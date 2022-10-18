from djitellopy import *

# Create a new instance of the tello drone, then connect to it.
tello = Tello()
tello.connect()

# Get basic info on the drone.  You can also use these getters during flight as well.
battery = tello.get_battery()
temperature = tello.get_temperature()
print("Battery: ", battery, "%")
print("Temperature: ", temperature, "°")


# Flight commands:

# Start by using takeoff to get the drone in the air.  Should hover around 30 cm in the air after takeoff.
tello.takeoff()

# Write what you want the drone to do here.  In this example the drone ascends 150 cm, moves forward 150 cm,
# rotates 180 degrees clockwise (turns around), moves forward 150 cm (back to its initial position),
# rotates counter-clockwise (turns back to initial orientation), and then descends by 150 cm (to initial takeoff height).

tello.move_up(150)
tello.move_forward(150)
tello.rotate_clockwise(180)
tello.move_forward(150)
tello.rotate_counter_clockwise(180)
tello.move_down(150)

# End by landing the drone. This also ends the process.
tello.land()
