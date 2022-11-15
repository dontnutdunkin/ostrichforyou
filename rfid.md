SDA--PIN 24
SCK--PIN 23
MOSI--PIN 19
MISO--PIN21
GND--PIN6
RST--PIN22
3.3v--PIN1 

connect the pins

stp 1: sudo raspi-config(to enable p4 spi)
stp 2: sudo reboot(to restart your raspberry pi)
stp 3: lsmod | grep spi ( to see if spi_bcm2835 is listed)
stp 4: sudo apt-get update 
        sudo apt-get update
stp 5: sudo apt-get install python3.pip (setting up the rfid reader)
stp 6: sudo pip3 install spidev (spidev library helps handle interaction with spi)
stp 7:sudo pip3 install mfrc522 (mfrc522.py which is an implementation of the rfid rc522 interface)


