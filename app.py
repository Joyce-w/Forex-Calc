from flask import Flask
from flask import render_template, request, redirect, flash, session
from forex import Forex
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']="chickenzarecool123"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False


@app.route("/")
def homepage():
    """Homepage for currency converter"""
    #rebind sessions
    curr_from = session['convert_from']
    curr_to = session['convert_to']
    amt = session['convert_amt']

    return render_template("home.html")


@app.route("/submission", methods=["POST"])
def data_submitted():
    """POST route for submitted data"""
    # save input to session
    session['convert_from'] = request.form['currency_from']
    session['convert_to'] = request.form['currency_to']
    session['convert_amt'] = request.form['amount']

    #rebind sessions
    curr_from = session['convert_from']
    curr_to = session['convert_to']
    amt = session['convert_amt']

    #create class out of submitted data
    submission = Forex(curr_from, curr_to, amt)

    #check if currency is valid
    check_curr_from = submission.check_valid_curr(curr_from)
    check_curr_to = submission.check_valid_curr(curr_to)
    
    if (check_curr_from is False):
        flash(f"{curr_from} is an invalid currency , try again.")

    if (check_curr_to is False):
        flash(f"{curr_to} is an invalid currency, try again.")

    #check if amt is valid
    check_amt = submission.check_amt(amt)
    if (check_amt is False):
        flash("Please enter a numerical amount to convert")

    return redirect("/")
