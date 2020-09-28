from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3


app = Flask(__name__)

app.config.from_object(__name__)
CORS(app)


def get_column_names(table_name, cursor):
    cursor.execute(f"pragma table_info({table_name})")
    return [row[1] for row in cursor.fetchall()]


@app.route("/")
def main():
    return (
        "<h1>Please go <a href='https://github.com/satorresja/Newshore'>"
        "here</a> to read the documentation."
    )


@app.route("/api/flights/<from_city>/<to_city>/<date>")
def get_flights(from_city, to_city, date):
    connector = sqlite3.connect("vuelos.db")
    cursor = connector.cursor()
    cursor.execute(
        f"""
        SELECT
            Flight.id,
            departure_station,
            arrival_station,
            price,
            departure_date,
            currency,
            Transport.number as flight_number
        FROM Flight
        JOIN Transport
        ON Flight.transport_id = Transport.id
        AND Flight.departure_station = '{from_city}'
        AND Flight.arrival_station = '{to_city}'
        AND Flight.departure_date = '{date}'
        ORDER BY flight_number
    """
    )

    result = cursor.fetchall()

    connector.close()
    if not result:
        return jsonify([])

    column_names = [
        "flight_id",
        "departure_station",
        "arrival_station",
        "price",
        "departure_date",
        "currency",
        "flight_number",
    ]
    data = [dict(zip(column_names, row)) for row in result]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
