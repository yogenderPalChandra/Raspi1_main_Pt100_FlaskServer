import time
import sys
import RPi.GPIO as GPIO
import sqlite3
from time import sleep

import board
import busio
import digitalio

import adafruit_max31865

import mysql.connector

conn = mysql.connector.connect(
  host="10.208.8.122",
  user="yogi",
  passwd="bittoo",
  database="TemaccessToRemoteRp2"
)

#print(db_connection)


c = conn.cursor()
#c.execute('DROP DATABASE temperature')
#c.execute("CREATE DATABASE temperature")
#conn = sqlite3.connect('temperature.db')
#c = conn.cursor()
date=time.strftime("%Y-%m-%d ")
t=time.strftime("%H:%M:%S")




# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs1 = digitalio.DigitalInOut(board.D4)  # Chip select of the MAX31865 board.
cs2 = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
cs3 = digitalio.DigitalInOut(board.D6)
cs4 = digitalio.DigitalInOut(board.D13)
cs5 = digitalio.DigitalInOut(board.D19)
cs6 = digitalio.DigitalInOut(board.D26)
cs7 = digitalio.DigitalInOut(board.D21)
cs8 = digitalio.DigitalInOut(board.D20)
cs9 = digitalio.DigitalInOut(board.D16)
cs10 = digitalio.DigitalInOut(board.D12)
cs11 = digitalio.DigitalInOut(board.D1)
cs12 = digitalio.DigitalInOut(board.D7)
cs13 = digitalio.DigitalInOut(board.D25)
cs14 = digitalio.DigitalInOut(board.D24)
cs15 = digitalio.DigitalInOut(board.D23)
cs16 = digitalio.DigitalInOut(board.D18)
cs17 = digitalio.DigitalInOut(board.D15)
cs18 = digitalio.DigitalInOut(board.D14)
cs19 = digitalio.DigitalInOut(board.D2)


sensor1 = adafruit_max31865.MAX31865(spi, cs1,  wires=4)
sensor2 = adafruit_max31865.MAX31865(spi, cs2,  wires=4)
sensor3 = adafruit_max31865.MAX31865(spi, cs3,  wires=4)
sensor4 = adafruit_max31865.MAX31865(spi, cs4,  wires=3)
sensor5 = adafruit_max31865.MAX31865(spi, cs5,  wires=4)
sensor6 = adafruit_max31865.MAX31865(spi, cs6,  wires=4)
sensor7 = adafruit_max31865.MAX31865(spi, cs7,  wires=4)
sensor8 = adafruit_max31865.MAX31865(spi, cs8,  wires=3)
sensor9 = adafruit_max31865.MAX31865(spi, cs9,  wires=4)
sensor10 = adafruit_max31865.MAX31865(spi, cs10,  wires=4)
sensor11 = adafruit_max31865.MAX31865(spi, cs11,  wires=4)
sensor12 = adafruit_max31865.MAX31865(spi, cs12,  wires=4)
sensor13 = adafruit_max31865.MAX31865(spi, cs13,  wires=4)
sensor14 = adafruit_max31865.MAX31865(spi, cs14,  wires=4)
sensor15 = adafruit_max31865.MAX31865(spi, cs15,  wires=4)
sensor16 = adafruit_max31865.MAX31865(spi, cs16,  wires=4)
sensor17 = adafruit_max31865.MAX31865(spi, cs17,  wires=4)
sensor18 = adafruit_max31865.MAX31865(spi, cs18,  wires=4)
sensor19 = adafruit_max31865.MAX31865(spi, cs19,  wires=4)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
# sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=2)

# Main loop to print the temperature every second.
#sql = 'DROP TABLE IF EXISTS temSensor;'
c.execute('DROP TABLE IF EXISTS temSensor;')
print ('table deleted')
c.execute('CREATE TABLE temSensor(id INT AUTO_INCREMENT PRIMARY KEY, Temp1d4 FLOAT, Temp2d5 FLOAT, Temp3d6 FLOAT, \
Temp4d13 FLOAT,  Temp5d19 FLOAT, Temp6d26 FLOAT, Temp7d21 FLOAT,Temp8d20 FLOAT,Temp9d16 FLOAT, \
Temp10d12 FLOAT,Temp11d1 FLOAT,Temp12d7 FLOAT, Temp13d8 FLOAT,Temp14d24 FLOAT,\
Temp15d23 FLOAT, Temp16d18 FLOAT,Temp17d15 FLOAT, Temp18d14 FLOAT,Temp19d2 FLOAT,Date DATE,Time TIME);')
conn.commit()

while True:
    # Read temperature.
    temp1 = sensor1.temperature
    temp2 = sensor2.temperature
    temp3 = sensor3.temperature
    temp4 = sensor4.temperature
    temp5 = sensor5.temperature
    temp6 = sensor6.temperature
    temp7 = sensor7.temperature
    temp8 = sensor8.temperature
    temp9 = sensor9.temperature
    temp10 = sensor10.temperature
    temp11 = sensor11.temperature
    temp12 = sensor12.temperature
    temp13 = sensor13.temperature
    temp14 = sensor14.temperature
    temp15 = sensor15.temperature
    temp16 = sensor16.temperature
    temp17 = sensor17.temperature
    temp18 = sensor18.temperature
    temp19 = sensor19.temperature
    #temp16 = sensor16.temperature
    #create tables and delete it if already exist
    #sql1 = 'DROP TABLE IF EXISTS temSensor'
    #c.execute(sql1)
    #c.execute('CREATE TABLE temSensor(id INTEGER PRIMARY KEY AUTOINCREMENT, Temp1 NUMERIC,Temp2 NUMERIC, Date DATE, Time TIME);')
    #c.execute(sql)
    #conn.commit()

    #CREATE TABLE temSensor(id INTEGER PRIMARY KEY AUTOINCREMENT, Temp1 NUMERIC,Temp2 NUMERIC, Date DATE, Time TIME);
    c.execute("INSERT INTO temSensor(Temp1d4, Temp2d5, Temp3d6,Temp4d13, \
    Temp5d19, Temp6d26,Temp7d21,Temp8d20, Temp9d16, Temp10d12,Temp11d1,Temp12d7,Temp13d8,Temp14d24, \
    Temp15d23, Temp16d18,Temp17d15, Temp18d14,Temp19d2,Date,Time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s, %s,%s,%s,%s)",\
    (temp1, temp2,temp3,temp4,temp5,temp6, temp7, temp8, temp9, temp10, temp11,temp12, temp13, temp14, temp15,temp16, temp17,temp18, temp19, date,t))
    # Print the value.
    conn.commit()
    print ('Top Source Tank:', temp4)
    print ('Bottom Source Tank:', temp8)
    print ('Top Testing HP circuit:', temp2)
    print ('Bottom Testing HP circuit:', temp3)
    print ('Top Testing load circuit:', temp6)
    print ('Bottom Testing load circuit:', temp9)
    print ('Load Tank tem.:', temp5)
    print ('Mix tem at load:', temp7)
    print('--------------------------')
    #print(stdout)
    sleep(0.5)
    #print("Temperature sensor1: {0:0.3f}C".format(temp1))
    #print("Temperature sensor 2: {0:0.3f}C".format(temp2))
    #print (type(temp1))
    # Delay for a second.
    #time.sleep(1.0)






