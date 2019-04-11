#!/usr/bin/env python
import sys

if sys.version_info[0] < 3:
    print("This script requires Python version 3.X or higher")
    sys.exit(1)

from bluepy import btle

class Robot(object):

    mac_addr = ''
    name = ''

    def __init__(self, mac_addr, name):
        self.mac_addr = mac_addr
        self.name = name

class RobotFinder(object):

    def __init__(self):
        self.robots = []

    def findRobots(self):
        scanner = btle.Scanner().withDelegate(btle.DefaultDelegate())
        devices = scanner.scan(10.0)

        for dev in devices:
            for (adtype, desc, value) in dev.getScanData():
                if(adtype == 9 and value.startswith('OzoEvo')):
                    print(adtype, dev.addr, value)
                    self.robots.append(Robot(dev.addr, value))

class RobotControl(object):
    TRANSMIT_UUID_DRIVE = "8903136c-5f13-4548-a885-c58779136702"
    TRANSMIT_UUID_CONTROL = "8903136c-5f13-4548-a885-c58779136703"

    def __init__(self, addr):
        self._mac = addr

    def connect(self):
        self._p = btle.Peripheral(self._mac, btle.ADDR_TYPE_RANDOM)
        self._p_transmit_drive = self._p.getCharacteristics(uuid=self.TRANSMIT_UUID_DRIVE)[0]
        self._p_transmit_control = self._p.getCharacteristics(uuid=self.TRANSMIT_UUID_CONTROL)[0]
        self.d = self._p_transmit_drive
        self.c = self._p_transmit_control
        
        # send stop file command to OzoBot to enable for sending commands
        self.c.write(b"\x50\x02\x01")

    def disconnect(self):
        pass

    def drive(self, leftWheel, rightWheel, duration):
        byteArray = []
        byteArray.append(64)
        byteArray.append(leftWheel & 255)
        byteArray.append(leftWheel >> 8 & 255)
        byteArray.append(rightWheel & 255)
        byteArray.append(rightWheel >> 8 & 255)
        byteArray.append(duration & 255)
        byteArray.append(duration >> 8 & 255)
        command = bytes(byteArray)
        return(command)

    def led(self, led, red, green, blue):
        byteArray = []
        byteArray.append(68)
        byteArray.append(led & 255)
        byteArray.append(led >> 8 & 255)
        byteArray.append(red)
        byteArray.append(green)
        byteArray.append(blue)
        command = bytes(byteArray)
        return(command)


