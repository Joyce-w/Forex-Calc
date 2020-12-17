from flask import Flask
from flask import render_template, request, redirect, flash, session
from forex import Forex
import requests
from forex_python.converter import CurrencyRates

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']="chickenzarecool123"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

c = CurrencyRates()

@app.route("/")
def homepage():
    """Homepage for currency converter"""
    #get country currency abbreviations from API
    res = requests.get("https://api.ratesapi.io/api/latest?base=USD")
    country_codes = res.json()['rates'].keys()


    return render_template("home.html", country_codes=country_codes)


@app.route("/submission")
def data_submitted():
    """POST route for submitted data"""
   
   # save input to session
    session['convert_from'] = request.args['convert_from']
    session['convert_to'] = request.args['convert_to']
    session['convert_amt'] = request.args['amt']

    #rebind sessions
    curr_from = session['convert_from']
    curr_to = session['convert_to']
    amt = session['convert_amt']

    print(amt, curr_to, curr_from)
    #create class out of submitted data
    submission = Forex(curr_from, curr_to, amt)

    # #check if currency is valid
    # check_curr_from = submission.check_valid_curr(curr_from)
    # check_curr_to = submission.check_valid_curr(curr_to)
    
    # if (check_curr_from is False):
    #     flash(f"{curr_from} is an invalid currency , try again.")

    # if (check_curr_to is False):
    #     flash(f"{curr_to} is an invalid currency, try again.")

    # #check if input currencies are the same
    # if (check_curr_from is check_curr_to):
    #     flash("Please select different currencies from each selection")

    # #check if amt is valid
    # check_amt = submission.check_amt(amt)
    # if (check_amt is False):
    #     flash("Please enter a numerical amount to convert")
    # convert
    session['conversion'] = round(c.convert(session['convert_from'], session['convert_to'], float(amt)), 2)

    return redirect("/")
