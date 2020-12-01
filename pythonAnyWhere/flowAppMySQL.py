from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template, send_file, make_response, request
app = Flask(__name__)
import sqlite3

import mysql.connector
import MySQLdb as db


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###Postgres shit@@@@@@@@@@@@@@
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#conn=sqlite3.connect('../temperature.db', check_same_thread=False)
#curs=conn.cursor()
# Retrieve LAST data from database
import os.path
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_MySQL_DATA_DIR = '/var/lib/mysql'
#print (BASE_DIR)
db_path = os.path.join(BASE_MySQL_DATA_DIR, "TemaccessToRemoteRp2")
#import mysql.connector

conn = mysql.connector.connect(
  host="10.208.8.122",
  user="yogi",
   passwd="bittoo",
  database="TemaccessToRemoteRp2"
)

#conn=sqlite3.connect(db_path, check_same_thread=False)
curs=conn.cursor()
#curs.execute("select * from temSensor")
#results = curs.fetchall()
#for r in results:
#    print (r)
#########################################################
####fetching flowrates by remotly connecting to RP2######
#########################################################
HOST = "10.208.8.121"
PORT = 3306
USER = "yogi"
PASSWORD = "bittoo"
DB = "allSensors"
connectionR = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
cR = connectionR.cursor()

'''
connectionR = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
cR = connectionR.cursor()
cR.execute("SELECT * FROM flowReadings ORDER BY id DESC LIMIT 1")
resultsR = cR.fetchall()
for rowR in resultsR:
      print (rowR)
'''
#print (db_path)
def getLastData():
        #conn=sqlite3.connect(db_path, check_same_thread=False)
        connectionR = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
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
def maxRowsTable():
	probably its counting the number of temp variables returned by   getLastData function  aka number of rows, temp is just random we can count first  variables 
	such as  id or whatever in temSensor

        curs.execute("select COUNT(id) from  temSensor")
        results  = curs.fetchall():
	for row in results:
		maxNumberRows=row[0]
	return maxNumberRows
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


'''

@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit]
        title_bar = ['Source tank top', 'Source tank bottom', 'Testing top HP Circuit', 'Testing bottom HP Circuit', 'Testing top Load Circuit', 'testing bottom load circuit']
        fig = plt.figure(figsize=(15,15))
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            plt.subplots_adjust( wspace = 1.0, hspace = 1.0)
            #fig.tight_layout()
            axis.set_title('Tem.: '+ title_bar[i])
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
'''





'''
@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit]
        fig = plt.figure(figsize=(15,10))
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            plt.subplots_adjust(top=0.4, wspace = 0.8, hspace = 0.7)
            #fig.tight_layout()
            axis.set_title('Tem.'+ plot_var[i], fontsize= 9)
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

'''

'''
@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit]
        fig = Figure(figsize=(10,3))
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            plt.subplots_adjust(top=0.4, wspace = 2.0, hspace = 2.0)
            #fig.tight_layout()
            axis.set_title('Tem.'+ str(plot_var[i]))
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

'''
'''
@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit]
        fig = Figure()
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            #fig.tight_layout()
            axis.set_title('Tem.'+ str(plot_var[i]), labelsize='small')
            axis.set_xlabel("Samples")
            axis.grid(True)
            #xs = range(numSamples)
            axis.plot(xs, ys)
            canvas = FigureCanvas(fig)
            output = io.BytesIO()
            canvas.print_png(output)
            response = make_response(output.getvalue())
            response.mimetype = 'image/png'
'''

'''
@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit]
        fig = Figure()
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            fig.tight_layout()
            axis.set_title('Tem.'+ str(plot_var[i]))
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


'''

'''
@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit]
        fig = Figure()
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            axis.set_title('Tem.'+ str(plot_var[i]), labelsize='small')
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
'''
'''
@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = ['tempTopSource', 'tempBottomSource', 'tempTopTestingHpCircuit', 'tempBottomTestingHpCircuit', 'tempTopTestingLoadCircuit', 'tempBottomLoadCircuit']
        fig = Figure()
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(2,3, i+1)
            axis.set_title('Temperature in C'+ plot_var[i])
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

'''
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)
