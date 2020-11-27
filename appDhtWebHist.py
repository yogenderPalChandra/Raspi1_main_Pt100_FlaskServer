from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template, send_file, make_response, request
app = Flask(__name__)
import sqlite3
#conn=sqlite3.connect('../temperature.db', check_same_thread=False)
#curs=conn.cursor()
# Retrieve LAST data from database
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "temperature.db")
conn=sqlite3.connect(db_path, check_same_thread=False)
curs=conn.cursor()
print (db_path)
def getLastData():
        conn=sqlite3.connect(db_path, check_same_thread=False)
        #conn=sqlite3.connect(db_path)
        curs=conn.cursor()
        for row in curs.execute("SELECT * FROM temSensor ORDER BY id DESC LIMIT 1"):
                id = str(row[0])
                date = str(row[-2])
                time = str(row[-1])
                tempAmbient = row[1]
                tempTopTestingHpCircuit = row[2]
                tempBottomTestingHpCircuit = row[3]
                tempTopSource = row[4]
                tempTLoadtank = row[5]
                tempTopTestingLoadCircuit = row[6]
                tempLoadMix= row[7]
                tempBottomSource = row[8]
                tempBottomLoadCircuit = row[9]
                temStrat1 =  row[10]
                temStrat3 =  row[11]
                temStrat5 =  row[12]
                temStrat7 =  row[13]
                temStrat9 =  row[14]
                temStrat11 =  row[15]
                temStrat13 =  row[16]
                temStrat15 =  row[17]
                temStrat17 =  row[18]
                temStrat19 =  row[19]
        conn.close()
        return id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1, temStrat3, temStrat5, temStrat7, temStrat9, temStrat11, temStrat13, temStrat15, temStrat17, temStrat19


def getHistData (numSamples):
	curs.execute("SELECT * FROM temSensor ORDER BY id DESC LIMIT "+str(numSamples))
	data = curs.fetchall()
	Id = []
	Date = []
	Time = []
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
		Date.append(row[-2])
		Time.append(row[-1])
		TempAmbient.append(row[1])
		TempTopTestingHpCircuit.append(row[2])
		TempBottomTestingHpCircuit.append(row[3])
		TempTopSource.append(row[4])
		TempTLoadtank.append(row[5])
		TempTopTestingLoadCircuit.append(row[6])
		TempLoadMix.append(row[7])
		TempBottomSource.append(row[8])
		TempBottomLoadCircuit.append(row[9])
		TemStrat1.append(row[10])
		TemStrat3.append(row[11])
		TemStrat5.append(row[12])
		TemStrat7.append(row[13])
		TemStrat9.append(row[14])
		TemStrat11.append(row[15])
		TemStrat13.append(row[16])
		TemStrat15.append(row[17])
		TemStrat17.append(row[18])
		TemStrat19.append(row[19])
	return Id, Date, Time, TempAmbient, TempTopTestingHpCircuit, TempBottomTestingHpCircuit , TempTopSource, TempTLoadtank, TempTopTestingLoadCircuit, TempLoadMix, TempBottomSource, TempBottomLoadCircuit , TemStrat1, TemStrat3, TemStrat5, TemStrat7, TemStrat9, TemStrat11, TemStrat13, TemStrat15, TemStrat17, TemStrat19

def maxRowsTable():
	'''probably its counting the number of temp variables returned by   getLastData function  aka number of rows, temp is just random we can count first  variables 
	such as  id or whatever in temSensor
	'''
	for row in curs.execute("select COUNT(id) from  temSensor"):
		maxNumberRows=row[0]
	return maxNumberRows
# define and initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
	numSamples = 100
@app.route("/")
def index():
    id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getLastData()
    templateData = {
        'id': id,
	'date': date,
	'time' : time,
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
	'StratT19':  temStrat19
        }
    return render_template('index.html', **templateData)



@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    global numSamples

    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getLastData()
    templateData = {
        'id': id,
        'date': date,
        'time' : time,
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
        'StratT19':  temStrat19
        }
    return render_template('index.html', **templateData)



@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        id, date, time, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19 = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit, tempTLoadtank, tempLoadMix]
        title_bar = ['Source tank top', 'Source tank bottom', 'Testing top HP Circuit', 'Testing bottom HP Circuit', 'Testing top Load Circuit', 'testing bottom load circuit', 'Load tank tem.', 'Mix Load tem.']
        fig = plt.figure(figsize=(15,15))
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)  
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(3,3, i+1)
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
