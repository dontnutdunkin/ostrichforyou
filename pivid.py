import time
from picamera import PiCamera
camera = PiCamera()
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video1.h264')
camera.wait_recording(10)
camera.stop_recording()
print("Finished Recording")

