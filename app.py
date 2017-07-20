# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:12:09 2017
@author: moghb
"""

from flask import Flask, render_template,url_for, redirect, request
import os
import json
import urllib
#import webbrowser

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
 
# You could import your python file (file.py) from here 
# import file

# defining data - json: just as an example
def getExchangeRates():
    response = urllib.request.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data, parse_float=float)
    return rdata

data2=[
  {
    "ID": "",
    "X": 79,
    "Y": 136,
    "Temperature": 130
  },
  {
    "ID": "",
    "X": 80,
    "Y": 167,
    "Temperature": 120
  },
  {
    "ID": "",
    "X": 72,
    "Y": 170,
    "Temperature": 100
  },
  {
    "ID": "",
    "X": 78,
    "Y": 184,
    "Temperature": 50
  },
  {
    "ID": "",
    "X": 81,
    "Y": 200,
    "Temperature": 210
  },
  {
    "ID": "",
    "X": 72,
    "Y": 278,
    "Temperature": 230
  },
  {
    "ID": "",
    "X": 68,
    "Y": 477,
    "Temperature": 80
  }
]

chart_display={"barchart": "none",
               "bubblechart":"run-in",
               "scatterchart":"run-in",
               "multilinechart":"run-in"
               }

sample = '{"info": {"level": "h1", "header": "Instrument information", "data": [{"header": "msManufacturer ", "value": "Thermo Finnigan", "level": "b"}, {"header": "msModel ", "value": "unknown", "level": "b"}, {"header": "msIonisation ", "value": "NSI", "level": "b"}, {"header": "msMassAnalyzer ", "value": "FTMS", "level": "b"}, {"header": "msDetector ", "value": "unknown", "level": "b"}]}, "qc": {"header": "Quality control", "level": "h1", "data": {"id_based": {"header": "ID-based quality control", "level": "h2", "data": [{"header": "Peptides identified", "value": 933, "level": "b"}, {"header": "Missed cleavages", "value": 132, "level": "b"}]}}}}';

@app.route("/chart")
def chart():
    # calling the function to acquire data inside a route
    display = json.dumps(chart_display)
    data = json.dumps(data2)
    rates = json.dumps(getExchangeRates())
    return render_template('chart.html',**locals()) 

@app.route("/output")
def output():
    template_sample = json.dumps(sample)
    return render_template('output.html',**locals() ) 

@app.route('/final', methods=['GET', 'POST'])
def final():
    if request.method == 'POST':
        return redirect(url_for('output')), redirect(url_for('chart'))
    return render_template('final.html')


if __name__ == "__main__":
    app.run()
    
# check http://127.0.0.1:5000/final in your browser after running this file