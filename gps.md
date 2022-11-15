VCC--PIN2
GND--PIN6
Rx--PIN 8
Tx--PIN10

stp 1: sudo raspi-config (to configure UART on rpi)(in this we have to interfacing option we have to go in seial p6 enable yes)
stp 2:sudo cat /dev/ttyAMA0 (to check the device type)
stp 3: ls -l /dev
