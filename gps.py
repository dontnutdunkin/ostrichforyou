import serial
from time import sleep
import webbrowser
import sys

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    nmea_time = []
    nmea_time = NMEA_buff[0]
    nmea_latitude = NMEA_buff[1]
    nmea_longitude = NMEA_buff[3]

    nema_latitude = 1905.1535
    nema_longitude = 7305.0250

    print("NMEA time: ", nmea_time,'\n')
    print("NMEA Latitude:", nmea_latitude,"NMEA Longitude:",nmea_longitude,'\n')

    lat = float(nmea_latitude)
    longi = float(nmea_longitude)

    lat_in_degree = convert_to_degree(lat)
    long_in_degree = convert_to_degree(longi)

def convert_to_degree(raw_value):
    decimal_value = raw_value/100.00
    degree = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degree + mm_mmmm
    position = "%.4f" %(position)
    return position


gpgga_info = "$GPGGA,"
ser = serial.Serial("/dev/ttyS0")
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degree = 0
long_in_degree = 0

try:
    while True:
        received_data = (str)(ser.readline())
        GPGGA_data_available = received_data.find(gpgga_info)
        
        if(GPGGA_data_available>0):
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
            NMEA_buff = (GPGGA_buffer.split(','))
            GPS_info()
            print("lat in degree:",lat_in_degree,"long in degree:",long_in_degree,'\n')
            map_link = 'http://maps.google.com/?q='+ lat_in_degree+','+long_in_degree
            print("<<<<<<<<<<<<<press ctrl+c to plot location on google map>>>>>>>>>>>>>>>\n")
            print("-------------------------------------\n")

except Keyboardinterupt:
    webbrowser.open(map_link)
sys.exit(0)
