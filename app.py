from flask import Flask
from flask import render_template, request, redirect, flash, session
from forex import Forex
import requests
from forex_python.converter import CurrencyRates, CurrencyCodes

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']="chickenzarecool123"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

cr = CurrencyRates()
cc = CurrencyCodes()

@app.route("/")
def homepage():
    """Homepage for currency converter"""
    try:
        #get country currency code from API
        res = requests.get("https://api.ratesapi.io/api/latest?base=USD")
    except:
        print("API server is down, please try again later.")

    country_codes = sorted(res.json()['rates'].keys())

    currencies = {curr_code: cc.get_currency_name(curr_code) for curr_code in country_codes}


    return render_template("home.html", currencies=currencies)


@app.route("/submission")
def data_submitted():
    """GET route for submitted data"""
   
    #save input to session
    session['convert_from'] = request.args['convert_from']
    session['convert_to'] = request.args['convert_to']

    if request.args['amt'] == '':
        flash("Please enter a larger amount to convert!")

    else:
        session['convert_amt'] = request.args['amt']

    #rebind sessions
    curr_from = session['convert_from']
    curr_to = session['convert_to']
    amt = session['convert_amt']

    #save name & symbol to session
    session['convert_from_symbol'] = cc.get_symbol(curr_from)
    session['convert_to_symbol'] = cc.get_symbol(curr_to)

    session['convert_from_name'] = cc.get_currency_name(curr_from)
    session['convert_to_name'] = cc.get_currency_name(curr_to)
    
    session['conversion'] = round(cr.convert(curr_from, curr_to, float(amt)), 2)



    #check if input currencies are the same
    if (curr_from == curr_to):
        flash("Please select different currencies from each selection.")

    #check if amount less than 0
    if (session['conversion'] <= 0):
        flash("The rate is less than 0. :( ")

    return redirect("/")
