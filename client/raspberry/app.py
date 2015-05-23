#/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import sys
import time
#ROOT = os.path.dirname(os.path.abspath(__file__))
#try:
#    import controller
#except ImportError:
#    sys.path.append(os.path.join(ROOT, ".."))
from websocket import create_connection
import test_ultrasound as ultrasound

TRIG1 = 20
ECHO1 = 21

TRIG2 = 12
ECHO2 = 16

TRIG3 = 23
ECHO3 = 24


TIME_BREAK = 0.3
WS_URL = "ws://192.168.1.100:9300/"


def main(url):
    server = create_connection(url)
    sensor = ultrasound.Ultrasound(TRIG1, ECHO1, TRIG2, ECHO2, TRIG3, ECHO3, TIME_BREAK)

    while True:
        distance1 = int(float(sensor.get_distances(TRIG1, ECHO1)))
        time.sleep(0.1)
        print("distance1 => ", distance1)
    	if distance1>5 or distance1<2:
			server.send(str(1))

        distance2 = int(float(sensor.get_distances(TRIG2, ECHO2)))
        time.sleep(0.1)
        print("distance2 => ", distance2)
		if distance2>5 or distance2<2:
			server.send(str(2))

        distance3 = int(float(sensor.get_distances(TRIG3, ECHO3)))
        time.sleep(0.1)
        print("distance3 => ", distance3)
		if distance3>5 or distance3<2:
			server.send(str(3))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else WS_URL)