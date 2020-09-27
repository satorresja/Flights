from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask, jsonify, render_template, flash, request
import json
import sqlite3
import reading


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app)
connector = sqlite3.connect('vuelosDisponibles10.db')
cursor = connector.cursor()
#c.execute('SELECT * FROM flight limit 1')
#data = c.fetchall()
def get_column_names(table_name, cursor):
    cursor.execute(f"pragma table_info({table_name})")
    return [row[1] for row in cursor.fetchall()]
table_name = "flight"
column_names = get_column_names(table_name, cursor)
cursor.execute(f"SELECT * FROM {table_name}")
data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
#rowDict = dict(zip([i[0] for i in c.description], data))




@app.route('/api/flights/')
def hello_world():
   return jsonify(data)
#@app.route("/gg", methods=["POST", "GET"])
#@app.route("/api/flights/", methods = ["POST"])


if __name__ == "__main__":
    app.run(debug=True, port=8080)