import time
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1280,720)
camera.start_preview()
time.sleep(5)
camera.capture('/home/pi/Desktop/ty2.jpg')
camera.stop_preview()
