#!/bin/bash
echo "Sending to CANhat"
sshpass -p inspectobot scp CAN_Driver.py pi@canhat.local:~/Rover/GM6020
