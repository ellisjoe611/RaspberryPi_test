import sys
import binascii
import struct
import time
from bluepy.btle import Scanner, DefaultDelegate, UUID, Peripheral
from ctypes import *

# C 라이브러리 불러오기
lib_coordinate = CDLL('./cooridnate.so')

led_service_uuid = UUID(0xA000)
led_char_uuid = UUID(0xA001)

# BLE 비콘장치들의 MAC 주소 저장
# stones : 위치 측정을 위한 기준점들 (좌, 중앙, 우)	->	모두 같은 간격으로 설치한다.
stones_mac = {"left" : "3C:A3:08:AC:73:7D" , "middle" : "3C:A3:08:AE:07:66" , "right" : "3C:A3:08:AC:8C:05"}
stones_rssi = {}
# devices : 새로 추가되는 장치들
devices_mac = {"all" : "00:00:00:00:00:00"}


def getStonesRssi():
	scanner = Scanner()
	devices = scanner.scan(10.0)

	count = 0
	for device in devices:
		if device.addr in stones_mac:

			count 

def getSvc(p):
	tempContainer = []
	services=p.getServices()
	#displays all services
	for service in services:
		tempContainer.append(str(service.uuid))
	return tempContainer.pop()

def getChar(p):
	tempContainer = []
	chList = p.getCharacteristics()
	for ch in chList:
		tempContainer.append(str(ch.uuid))
	return tempContainer.pop()




print("Setting up connection with beacon stones...")
p = Peripheral(sys.argv[1], "public")
led_service_uuid = getSvc(p)
led_char_uuid = getChar(p)


print("SVC : " + led_service_uuid + " / Char : " + led_char_uuid)
print("Setup is complete. Starting service...")

LedService=p.getServiceByUUID(led_service_uuid)


try:
	ch = LedService.getCharacteristics(led_char_uuid)[0]
	while True:
		ch.write(struct.pack('<B', 0x00));
		print ("Led2 on")
		time.sleep(2)
		ch.write(struct.pack('<B', 0x01));
		print ("Led2 off")
		time.sleep(2)
except (KeyboardInterrupt, SystemExit):
	print("Pressed keyboard for interruption!")
finally:
	p.disconnect()
	print("Terminating program...")
