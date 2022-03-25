#Reference: https://github.com/tlack/PPO-positioner-GM6020

import os
import can
import time

duration = 5

motVals = [30000, 30000, -30000, -30000] #Motor power values -30000 to 30000

def motVal2can(Vals):

	output = [0] * (2*len(Vals))

	for i in range(len(Vals)):
		num = Vals[i]

		if num > 30000:
			num = 30000
		elif num < -30000:
			num = -30000

		if num > 0: #Positive
			output[2*i] = int("{0:016b}".format(num)[:8],2) #Higher order byte
			output[2*i+1] = int("{0:016b}".format(num)[8:],2) #Lower order byte

		else: #Negative
			num = abs(num)
			output[2*i] =	int(bin((num ^ 65535) + 1)[2:10],2) #Higher order byte
			output[2*i+1] =	int(bin((num ^ 65535) + 1)[10:],2) #Lower order byte
					
	return output

# print(motVal2can(motVals))

#Check if can0 is up
with open('/sys/class/net/can0/operstate','r') as f:
	can0status = f.read()

if can0status == "down\n":
	# Create a can link on can0
	os.system('sudo ip link set can0 up type can bitrate 1000000   dbitrate 8000000 restart-ms 1000 berr-reporting on fd on')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native

while(True):
	msg = can.Message(arbitration_id=0x1ff, dlc=8, data=motVal2can(motVals), is_extended_id=False)
	# msg = can.Message(arbitration_id=0x1ff, dlc=8, data=[39, 16, 0, 0, 0, 0, 0, 0], is_extended_id=False)
	can0.send_periodic(msg,.01,duration)

os.system('sudo ifconfig can0 down')