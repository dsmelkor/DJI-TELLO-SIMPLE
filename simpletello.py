from djitellopy import Tello

import time

tello = Tello()
#---------------------------

tello.connect()

tello.get_battery()

tello.get_barometer ()

tello.get_distance_tof()


tello.takeoff()
time.sleep(6)

tello.move_forward(160)
time.sleep(6)

tello.move_up (40)
time.sleep(5)

tello.move_forward(210)
time.sleep(6)

tello.rotate_counter_clockwise(45)
time.sleep(5)

tello.move_forward(50)
time.sleep(6)

tello.rotate_counter_clockwise(45)
time.sleep(5)

tello.move_forward(50)
time.sleep(6)



tello.land()
time.sleep(5)


tello.end()
