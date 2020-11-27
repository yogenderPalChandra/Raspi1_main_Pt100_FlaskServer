from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template, send_file, make_response, request
app = Flask(__name__)
import sqlite3

import mysql.connector
import MySQLdb as db

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
HOST = "10.208.8.121"
PORT = 3306
USER = "yogi"
PASSWORD = "bittoo"
DB = "allSensors"
#connectionR = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
#cR = connectionR.cursor()


connectionR = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
cR = connectionR.cursor()
#cR.execute("SELECT * FROM flowReadings ORDER BY id DESC LIMIT 1")
cR.execute("SELECT * FROM flowReadings")
resultsR = cR.fetchall()
for rowR in resultsR:
      print (rowR)


