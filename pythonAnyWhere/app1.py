from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template, send_file, make_response, request
#app = Flask(__name__)
#import sqlite3

#import mysql.connector
#import MySQLdb as dB
import os
print ('ok')
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###Postgres shit@@@@@@@@@@@@@@
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import allSensors
#conn=sqlite3.connect('../temperature.db', check_same_thread=False)
#curs=conn.cursor()
# Retrieve LAST data from database
import os.path
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#BASE_MySQL_DATA_DIR = '/var/lib/mysql'
#print (BASE_DIR)
#db_path = os.path.join(BASE_MySQL_DATA_DIR, "TemaccessToRemoteRp2")
#import mysql.connector
'''
conn = mysql.connector.connect(
  host="10.208.8.122",
  user="yogi",
   passwd="bittoo",
  database="TemaccessToRemoteRp2"
)
'''
#conn=sqlite3.connect(db_path, check_same_thread=False)
#curs=conn.cursor()
#curs.execute("select * from temSensor")
#results = curs.fetchall()
#for r in results:
#    print (r)
#########################################################
####fetching flowrates by remotly connecting to RP2######
#########################################################
'''
HOST = "10.208.8.121"
PORT = 3306
USER = "yogi"
PASSWORD = "bittoo"
DB = "allSensors"
connectionR = dB.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
cR = connectionR.cursor()

connectionR = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
cR = connectionR.cursor()
cR.execute("SELECT * FROM flowReadings ORDER BY id DESC LIMIT 1")
resultsR = cR.fetchall()
for rowR in resultsR:
      print (rowR)
'''

##@@@@@@@@@@@@@@@@@@@@@
##Postgres in app.py@@@
##@@@@@@@@@@@@@@@@@@@@@

import sys
import RPi.GPIO as GPIO
#import sqlite3
from time import sleep

import board
import busio
import digitalio

import adafruit_max31865

import psycopg2

#import mysql.connector

print ('ok')
#@app.route("/data/db")

'''
def readPin():

    #print(db_connection)
    conn = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "10.208.8.122", port = "5432")
    print ("Opened database successfully")
    c = conn.cursor()
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
    sensor19 = adafruit_max31865.MAX31865(spi, cs19,  wires=4
    #dropTableStmt   = "DROP TABLE IF EXISTS %s;"%sensors;
    #c.execute('DROP TABLE IF EXISTS "sensors";')
    #c.execute(dropTableStmt)
    #print ('table deleted')

    #conn.commit()

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

        c.execute("INSERT INTO temSensor(Temp1d4, Temp2d5, Temp3d6,Temp4d13, \
        Temp5d19, Temp6d26,Temp7d21,Temp8d20, Temp9d16, Temp10d12,Temp11d1,Temp12d7,Temp13d8,Temp14d24, \
        Temp15d23, Temp16d18,Temp17d15, Temp18d14,Temp19d2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s, %s,%s)",\
        (temp1, temp2,temp3,temp4,temp5,temp6, temp7, temp8, temp9, temp10, temp11,temp12, temp13, temp14, temp15,temp16, temp17,temp18, temp19))

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
        sleep(0.1)
#    return render_template('index.html.html', **templateData)

'''
'''


#print (db_path)
def getLastData():
        #conn=sqlite3.connect(db_path, check_same_thread=False)
        connectionR = dB.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
        cR = connectionR.cursor()
        cR.execute("SELECT * FROM flowReadings ORDER BY id DESC LIMIT 1")
        resultsR = cR.fetchall()
        for rowR in resultsR:
                idR = str(rowR[0])
                dateTimeR = str(rowR[1])
                flowHP = rowR[2]
                flowLoad = rowR[3]
        connectionR.close()
        conn = mysql.connector.connect(host="10.208.8.122",user="yogi",passwd="bittoo",database="TemaccessToRemoteRp2")
        #conn=sqlite3.connect(db_path)
        curs=conn.cursor()
        curs.execute("SELECT * FROM temSensor ORDER BY id DESC LIMIT 1")
        results  = curs.fetchall()
        for row in results:
                id = str(row[0])
                dateTime = str(row[1])
                #time = str(row[-1])
                tempAmbient = row[2]
                tempTopTestingHpCircuit = row[3]
                tempBottomTestingHpCircuit = row[4]
                tempTopSource = row[5]
                tempTLoadtank = row[6]
                tempTopTestingLoadCircuit = row[7]
                tempLoadMix= row[8]
                tempBottomSource = row[9]
                tempBottomLoadCircuit = row[10]
                temStrat1 =  row[11]
                temStrat3 =  row[12]
                temStrat5 =  row[13]
                temStrat7 =  row[14]
                temStrat9 =  row[15]
                temStrat11 =  row[16]
                temStrat13 =  row[17]
                temStrat15 =  row[18]
                temStrat17 =  row[19]
                temStrat19 =  row[20]
        conn.close()
        return id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1, temStrat3, temStrat5, temStrat7, temStrat9, temStrat11, temStrat13, temStrat15, temStrat17, temStrat19, flowHP, flowLoad



def getHistData (numSamples):
	curs.execute("SELECT * FROM temSensor ORDER BY id DESC LIMIT "+str(numSamples))
	data = curs.fetchall()
	Id = []
	DateTime = []
	#Time = []
	TempAmbient = []
	TempTopTestingHpCircuit = []
	TempBottomTestingHpCircuit = []
	TempTopSource =  []
	TempTLoadtank = []
	TempTopTestingLoadCircuit = []
	TempLoadMix = []
	TempBottomSource = []
	TempBottomLoadCircuit = []
	TemStrat1 = []
	TemStrat3 = []
	TemStrat5 = []
	TemStrat7 = []
	TemStrat9 = []
	TemStrat11 = []
	TemStrat13 = []
	TemStrat15 = []
	TemStrat17 = []
	TemStrat19 = []
	for row in reversed(data):
		Id.append(row[0])
		DateTime.append(row[1])
		#Time.append(row[-1])
		TempAmbient.append(row[2])
		TempTopTestingHpCircuit.append(row[3])
		TempBottomTestingHpCircuit.append(row[4])
		TempTopSource.append(row[5])
		TempTLoadtank.append(row[6])
		TempTopTestingLoadCircuit.append(row[7])
		TempLoadMix.append(row[8])
		TempBottomSource.append(row[9])
		TempBottomLoadCircuit.append(row[10])
		TemStrat1.append(row[11])
		TemStrat3.append(row[12])
		TemStrat5.append(row[13])
		TemStrat7.append(row[14])
		TemStrat9.append(row[15])
		TemStrat11.append(row[16])
		TemStrat13.append(row[17])
		TemStrat15.append(row[18])
		TemStrat17.append(row[19])
		TemStrat19.append(row[20])
	cR.execute("SELECT * FROM flowReadings  ORDER BY id DESC LIMIT "+str(numSamples))
	dataR = cR.fetchall()
	IdR = []
	DateTimeR = []
	flowHP = []
	flowLoad = []
	for rowR in reversed(dataR):
		IdR.append(rowR[0])
		DateTimeR.append(rowR[1])
		#Time.append(row[-1])
		flowHP.append(rowR[2])
		flowLoad.append(rowR[3])

	return Id, DateTime, TempAmbient, TempTopTestingHpCircuit, TempBottomTestingHpCircuit , TempTopSource, TempTLoadtank, TempTopTestingLoadCircuit, TempLoadMix, TempBottomSource, TempBottomLoadCircuit , TemStrat1, TemStrat3, TemStrat5, TemStrat7, TemStrat9, TemStrat11, TemStrat13, TemStrat15, TemStrat17, TemStrat19, flowHP, flowLoad
'''
'''
def maxRowsTable():
	probably its counting the number of temp variables returned by   getLastData function  aka number of rows, temp is just random we can count first  variables 
	such as  id or whatever in temSensor

        curs.execute("select COUNT(id) from  temSensor")
        results  = curs.fetchall():
	for row in results:
		maxNumberRows=row[0]
	return maxNumberRows
'''
'''
def maxRowsTable():
    curs.execute("select COUNT(id) from  temSensor")
    results  = curs.fetchall()
    for row in results:
        maxNumberRows=row[0]
    return maxNumberRows
# define and initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
	numSamples = 100
@app.route("/")
def index():
    id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19, flowHP, flowLoad = getLastData()
    templateData = {
        'id': id,
	'dateTime': dateTime,
	#'time' : time,
	'AmbientTem':tempAmbient,
	'TopTestingtemHPcircuit':tempTopTestingHpCircuit,
	'BottomtestingtemHPcircuit': tempBottomTestingHpCircuit,
	'TemTopSource': tempTopSource,
	'LoadtankTem': tempTLoadtank,
	'Toptemoftestingtankloadcircuit': tempTopTestingLoadCircuit,
	'Mixtematload': tempLoadMix,
	'sourcetankbottomtemp': tempBottomSource,
	'Testingbottomloadcircuit': tempBottomLoadCircuit,
	'StratT1': temStrat1,
	'StratT3': temStrat3,
	'StratT5':  temStrat5,
	'StratT7':  temStrat7,
	'StratT9':  temStrat9,
	'StratT11':  temStrat11,
	'StratT13':  temStrat13,
	'StratT15':  temStrat15,
        'StratT17':  temStrat17,
	'StratT19':  temStrat19,
        'FlowHP': flowHP,
        'FlowLoad': flowLoad
        }
    return render_template('index.html', **templateData)



@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    global numSamples

    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19, flowHP, flowLoad = getLastData()
    templateData = {
        'id': id,
        'dateTime': dateTime,
        #'time' : time,
        'AmbientTem':tempAmbient,
        'TopTestingtemHPcircuit': tempTopTestingHpCircuit,
        'BottomtestingtemHPcircuit': tempBottomTestingHpCircuit,
        'TemTopSource': tempTopSource,
        'LoadtankTem': tempTLoadtank,
        'Toptemoftestingtankloadcircuit': tempTopTestingLoadCircuit,
        'Mixtematload': tempLoadMix,
        'sourcetankbottomtemp': tempBottomSource,
        'Testingbottomloadcircuit': tempBottomLoadCircuit,
        'StratT1': temStrat1,
        'StratT3': temStrat3,
        'StratT5':  temStrat5,
        'StratT7':  temStrat7,
        'StratT9':  temStrat9,
        'StratT11':  temStrat11,
        'StratT13':  temStrat13,
        'StratT15':  temStrat15,
        'StratT17':  temStrat17,
        'StratT19':  temStrat19,
        'FlowHP': flowHP,
        'FlowLoad': flowLoad
        }
    return render_template('index.html', **templateData)



@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19, flowHP, flowLoad = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit, tempTLoadtank, tempLoadMix, flowHP, flowLoad]
        title_bar = ['Source tank top', 'Source tank bottom', 'Testing top HP Circuit', 'Testing bottom HP Circuit', 'Testing top Load Circuit', 'testing bottom load circuit', 'Load tank tem.', 'Mix Load tem.', 'HP flow rate ','Load Flow Rate']
        fig = plt.figure(figsize=(15,15))
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(3,4, i+1)
            plt.subplots_adjust( wspace = 1.0, hspace = 1.0)
            #fig.tight_layout()
            axis.set_title(title_bar[i])
            axis.set_xlabel("Samples")
            axis.grid(True)
            #xs = range(numSamples)
            axis.plot(xs, ys)
            canvas = FigureCanvas(fig)
            output = io.BytesIO()
            canvas.print_png(output)
            response = make_response(output.getvalue())
            response.mimetype = 'image/png'
        return response



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)
'''
