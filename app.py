# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:12:09 2017

@author: moghb
"""

from flask import Flask, render_template
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
    rates = []
    response = urllib.request.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data, parse_float=float)
 
    rates.append( rdata['rates']['USD'] )
    rates.append( rdata['rates']['GBP'] )
    rates.append( rdata['rates']['HKD'] )
    rates.append( rdata['rates']['AUD'] )
    return rates
 
@app.route("/")
def multi_charts():
    # calling the function to acquire data inside a route
    rates = getExchangeRates()
    return render_template('test.html',**locals())   

if __name__ == "__main__":
    app.run()
    
# check http://127.0.0.1:5000/ in your browser after running this file
