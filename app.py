from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)

app.config['SECRET_KEY']="chickenzarecool123"

debug = DebugToolbarExtension(app)