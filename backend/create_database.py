import random
import sqlite3
import click

from faker import Faker
from tqdm import tqdm

fake = Faker()


CITIES = ["Bogota", "Medellin", "Manizales"]

TRANSPORT_CONTRACT = """
    CREATE TABLE Transport (
        id      INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        number  VARCHAR(20) UNIQUE
    );
"""


FLIGHT_CONTRACT = """
    CREATE TABLE Flight (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        departure_station   VARCHAR(20),
        arrival_station     VARCHAR(20),
        price               INTEGER,
        departure_date      DATE,
        currency            VARCHAR(20),
        transport_id        INTEGER
    );
"""

@click.command()
@click.option("--num_transports", default=100, show_default=True)
@click.option("--num_flights", default=1000, show_default=True)
def main(num_transports, num_flights):
    connection = sqlite3.connect("vuelos.db")
    cursor = connection.cursor()

    cursor.executescript(
        f"""
        DROP TABLE IF EXISTS Transport;
        DROP TABLE IF EXISTS Flight;
        {TRANSPORT_CONTRACT}
        {FLIGHT_CONTRACT}
    """
    )
    connection.commit()

    for _ in tqdm(range(num_transports)):
        cursor.executescript(
            f"""
            INSERT INTO Transport (number) VALUES ('{fake.license_plate()}');
        """
        )
        connection.commit()

    for _ in tqdm(range(num_flights)):
        from_city = random.choice(CITIES)
        to_city = random.choice(list(set(CITIES) - {from_city}))
        date = fake.date_between(start_date="today", end_date="+1y")
        cursor.executescript(
            f"""
            INSERT INTO Flight (
                departure_station,
                arrival_station,
                price,
                departure_date,
                currency,
                transport_id
            )
            VALUES (
                '{from_city}',
                '{to_city}',
                {random.randint(50, 100) * 1000},
                '{date}',
                'COP',
                {random.randint(1, num_transports)}
            );
        """
        )
        connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
