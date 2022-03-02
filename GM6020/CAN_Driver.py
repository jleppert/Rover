#Reference: https://github.com/tlack/PPO-positioner-GM6020

import os
import can
import time

duration = 5


class Motor ():

#Create a can link on can0
os.system('sudo ip link set can0 up type can bitrate 1000000   dbitrate 8000000 restart-ms 1000 berr-reporting on fd on')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native

msg = can.Message(arbitration_id=0x1ff, dlc=8, data=[39, 16, 0, 0, 0, 0, 0, 0], is_extended_id=False)
can0.send_periodic(msg,.01,duration)

time.sleep(duration)

os.system('sudo ifconfig can0 down')