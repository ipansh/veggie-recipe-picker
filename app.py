from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/submitinfo", methods = ['POST'])
def submit():
    #message = request.form.values()[0]
    return render_template('result.html')

if __name__  == '__main__': 
    app.run(debug=True)