from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vuelosDisponibles3.db"
db = SQLAlchemy(app)

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.String(20))
    flights = db.relationship("Flight", backref="traveler")
    

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    departureStation = db.Column(db.String(20))
    arrivalStation = db.Column(db.String(20))
    departureDate = db.Column(db.String(20))
    prize = db.Column(db.Integer)
    currency = db.Column(db.Integer)
    traveler_id = db.Column(db.Integer, db.ForeignKey("transport.id"))



firstFly = Transport(number="A1234")
secondFly = Transport(number="B1234")


#departureStation_1 = Flight(departureStation="MEDELLIN", traveler=firstFly)
#arrivalStation = 
#departureDate = 
#prize = 
#currency = 


    
db.session.add(firstFly)
db.session.add(secondFly)
db.session.commit()
            
#db.create_all()


"""class Transport:
    def __init__(self):
        self.id=0
        print("Hey prro") 
    
    def flight(self):
        ciudades = int(input("Ingrese la cantidad de ciudades: "))
        for i in range(ciudades):
            departureStation = str(input("Ingresar las ciudades disponibles: "))
            self.departureStation = departureStation

        arrivalStation = []
        arrivalStation.append(ciudades)
        print(departureStation)
        departureDate = ["2020/09/28","2020/09/29","2020/09/30","2020/10/01","2020/10/02"]
        prize = [10000,20000,15000]
        currency = ["COP"]
        

Transport().flight()"""