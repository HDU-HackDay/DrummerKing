#/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import sys
import time
import websocket
#from websocket import create_connection
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
    #websocket.enableTrace(True)
    server = websocket.create_connection(url)
    sensor = ultrasound.Ultrasound(TRIG1, ECHO1, TRIG2, ECHO2, TRIG3, ECHO3, TIME_BREAK)
    while True:
        distance1 = float(sensor.get_distances(TRIG1, ECHO1))
        print("distance1 => ", distance1)
        if distance1>4:
        print("1")
        try:
            server.send(str(1))
        except EOFError:
            print("error =>", EOFError)
        time.sleep(0.3)
    else:
        time.sleep(0.2)

        distance2 = float(sensor.get_distances(TRIG2, ECHO2))
        print("distance2 => ", distance2)
    if distance2>3.3:
        try:
            server.send(str(2))
        except EOFError:
            print("error =>", EOFError)
        print("2")
        time.sleep(0.3)
    else:
        time.sleep(0.2)

        distance3 = float(sensor.get_distances(TRIG3, ECHO3))
        print("distance3 => ", distance3)
    if distance3>3.3:
        print("3")
        try:
            server.send(str(3))
        except EOFError:
            print("error =>", EOFError)
        time.sleep(0.3)
    else:
        time.sleep(0.2)

    server.close()
if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else WS_URL)