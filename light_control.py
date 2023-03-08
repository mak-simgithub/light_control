# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:33:22 2023

@author: LucaSomm
"""

import time
import serial
import sys

ser = serial.Serial(
    port ='/dev/ttyS0',
    baudrate = 19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

text = input("Which DALI address ( 0-63, 127=All) : ")
address = int(text)*2
input = 254
ser.read(100)
y1 = 0
y3 = 0

while input < 255 :

    text = raw_input(" What level : ")
    if text == "q":
        exit()
    if text == "":
        input = input+1
        print('set   level : %d'%input)
    else:
        input = int(text,10)

    ser.write('h%02X%02X\n'%(address,input))