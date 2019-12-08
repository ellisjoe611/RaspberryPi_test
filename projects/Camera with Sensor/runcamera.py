import RPi.GPIO as GPIO   
import time, os, sys, glob
from datetime import datetime 
import picamera
import subprocess

#define necessary parameters
pinNum = 18	#set GPIO_18 as the input of 'HC-SR501'

#define camera function
def createH264(name):
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	camera.framerate = 30
	camera.awb_mode = 'auto'

	camera.start_recording(name + '.h264')
	camera.wait_recording(5)
	camera.stop_recording()
#end of createVideo()

#define function for deleting .h264 file
def deleteH264(name):
	if os.path.isfile(name + '.h264'):
		os.remove(name + '.h264')
def deleteH264_all():
	files = glob.iglob(os.path.join('./', '*.h264'))
	for file in files:
		if os.path.isfile(file):
			os.remove(file)

#start main processing...
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.IN)
print("Setting up all sensors...")
time.sleep(5)

#start main processing...
try:
	while True:
		#if detected...
		if GPIO.input(pinNum):
			#first, create .h264 video
			now = datetime.now()
			fileName = '%s-%s-%s_%s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
			print("Human is detected! Recording 5-sec video...")
			createH264(fileName)

			#Then, convert *.264 -> *.mp4
			if subprocess.call(['MP4Box','-add', fileName + '.h264', fileName + '.mp4']) == 0:
				print("Created video named \'%s.mp4\'" % fileName)
				deleteH264(fileName)
			else:
				print("Error: failed converting...")
				deleteH264(fileName)
		#if NOT detected...
		else:
			print("Nothing...")
		
		time.sleep(1)
	#end of while

#list of possible exceptions
except KeyboardInterrupt:
	print("Pressed Keyboard.")
except TimeoutError:
	print("TIMEOUT!! Check out the error and try again...")
except:
	print("Error: unknown error...")

GPIO.cleanup()
deleteH264_all()
print("Good bye~")
sys.exit()