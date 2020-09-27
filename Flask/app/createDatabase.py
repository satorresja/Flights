from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import warnings
from flask import Flask, jsonify, render_template, flash, request
import json

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
    
warnings.filterwarnings("ignore")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vuelosDisponibles10.db"
db = SQLAlchemy(app)


class Transport(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.String(20))
    flights = db.relationship("Flight", backref="fly")
    

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    departureStation = db.Column(db.String(20))
    arrivalStation = db.Column(db.String(20))
    departureDate = db.Column(db.String(20))
    prize = db.Column(db.Integer)
    currency = db.Column(db.Integer)
    fly_id = db.Column(db.Integer, db.ForeignKey("transport.id"))



firstFly = Transport(number="A1234")
secondFly = Transport(number="B1234")


passenger_1 = Flight(
    departureStation="MEDELLIN", 
    arrivalStation="BOGOTA", 
    departureDate="2020/09/28",
    prize=200000,
    currency="COP",
    fly=firstFly)

passenger_2 = Flight(
    departureStation="MEDELLIN", 
    arrivalStation="BOGOTA", 
    departureDate="2020/09/28",
    prize=200000,
    currency="COP",
    fly=firstFly)

secondRoute = Flight(
    departureStation="BOGOTA", 
    arrivalStation="MEDELLIN", 
    departureDate="2020/09/28",
    prize=200000,
    currency="COP",
    fly=secondFly)

secondRoute_1 = Flight(
    departureStation="BOGOTA", 
    arrivalStation="MEDELLIN", 
    departureDate="2020/09/28",
    prize=200000,
    currency="COP",
    fly=secondFly)





db.create_all()   
db.session.add(firstFly)
db.session.add(secondFly)
db.session.commit()



if __name__ == "__main__":
    app.run(debug=True, port=6969)
