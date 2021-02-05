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
        #country currency code source used in conjunction with forex-python library 
        res = requests.get("https://api.ratesapi.io/api/latest?base=USD")
    except:
        print("API server is down, please try again later.")

    # alphabatize currency codes for user friendliness
    country_codes = sorted(res.json()['rates'].keys())

    # create dict consisiting of currency symbol and its coresponding name
    currencies = {curr_code: cc.get_currency_name(curr_code) for curr_code in country_codes}

    return render_template("home.html", currencies=currencies)


@app.route("/submission")
def data_submitted():
    """GET route for submitted data"""
   
    #save form input values to session
    session['convert_from'] = request.args['convert_from']
    session['convert_to'] = request.args['convert_to']

    # notify user of empty conversion amount
    if request.args['amt'] == '':
        flash("Please enter an amount to convert!")


    else:
        session['convert_amt'] = request.args['amt']

    #rebind session data
    curr_from = session['convert_from']
    curr_to = session['convert_to']
    amt = session['convert_amt']
    amt = float(amt)

    #check if amount less than 0
    if (amt <= 0):
        flash("Please enter a rate greater than 0.")

    #check if input currencies are the same and display error 
    if (curr_from == curr_to):
        flash("Please select different currencies from each selection.")

    #save currency symbols & names to session
    session['convert_from_symbol'] = cc.get_symbol(curr_from)
    session['convert_to_symbol'] = cc.get_symbol(curr_to)

    session['convert_from_name'] = cc.get_currency_name(curr_from)
    session['convert_to_name'] = cc.get_currency_name(curr_to)
    
    # calculate conversion rate from session data, limit to 2 place values
    session['conversion'] = round(cr.convert(curr_from, curr_to, amt), 2)
    
    return redirect("/")
