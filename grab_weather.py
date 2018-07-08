#!/usr/bin/python3
from subprocess import call
import requests
from time import gmtime, strftime
import json
r = requests.get('http://192.168.1.137:5000/record')
data = r.json()[0]
path= 'KI7ADJ>APX208,WIDE2-2*:'

lat = 'XXXXXXX'
long = 'XXXXXXX'
lux = (data['lux'])
lux = str(round(float(lux)))
if (int(lux) >999):
    lux = "l" + lux
else:
    lux = "L" + lux

press=(data['prs'])
press = str(round(float(press)*10))
hum=str(data['hum'])
hum = str(round(float(hum)))
temp= data['tmp']
temp = float(temp)
temp = str(int(round(temp * 1.8 + 32)))
if (int(temp) < 99):
    temp = "0" + temp
time = strftime('%d%H%M', gmtime())
print ('@'+time+'z'+lat+'/'+long+'_.../...g...t'+temp+lux+'p...P...h'+hum+'b'+press+'0.duino')
