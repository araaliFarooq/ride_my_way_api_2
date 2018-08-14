import psycopg2
from pprint import pprint
from app import app
# from config import app_config


class DBConnection:
    def __init__(self):
        self.con = psycopg2.connect(database="farooq", user="postgres", password="12345", host="localhost", port="5432")

        self.con.autocommit = True
        self.cursor = self.con.cursor()
        # self.dict_cursor = self.con.cursor(cursor_factory=extra.DictCursor)

    def create_tables(self):

        queries = (
            """
            CREATE TABLE IF NOT EXISTS clients (
                client_id SERIAL PRIMARY KEY,
                firstName VARCHAR(50) NOT NULL,
                secondName VARCHAR(50) NOT NULL,
                userName VARCHAR(50) NOT NULL UNIQUE,
                contact VARCHAR(15) NOT NULL UNIQUE,
                password VARCHAR(25) NOT NULL
            )
            """,

            """
			CREATE TABLE IF NOT EXISTS drivers (
				driver_id SERIAL PRIMARY KEY,
					firstName VARCHAR(50) NOT NULL,
					secondName VARCHAR(50) NOT NULL,
					userName VARCHAR(50) NOT NULL UNIQUE,
					contact VARCHAR(15) NOT NULL UNIQUE,
					carType VARCHAR(25) NOT NULL,
					regNumber VARCHAR(25) NOT NULL UNIQUE,
					licNumber VARCHAR(25) NOT NULL UNIQUE,
					password VARCHAR(25) NOT NULL			
						)
						""",

            """
            CREATE TABLE IF NOT EXISTS rideOffers (
                ride_id SERIAL PRIMARY KEY,
                driver_id INTEGER NOT NULL,
                date timestamp NOT NULL,
                driverName VARCHAR(50) NOT NULL,
                location VARCHAR(50) NOT NULL,
                carType VARCHAR(50) NOT NULL,
                plateNumber VARCHAR(50) NOT NULL,
                contact VARCHAR(50) NOT NULL,
                availability VARCHAR(20) NOT NULL,
                costPerKm VARCHAR(20) NOT NULL,
                FOREIGN KEY (driver_id)
                    REFERENCES drivers (driver_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS rideRequests (
                request_id SERIAL PRIMARY KEY,
                date timestamp NOT NULL,
                ride_id INTEGER NOT NULL,
                client_id INTEGER NOT NULL,
                client_name VARCHAR(50) NOT NULL,
                client_contact VARCHAR(30) NOT NULL,
                location VARCHAR(30) NOT NULL,
                destination VARCHAR(30) NOT NULL,
                status VARCHAR(30) NOT NULL,
                FOREIGN KEY (ride_id)
                    REFERENCES rideOffers (ride_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (client_id)
                    REFERENCES clients (client_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)

    def delete_tables(self):

        delete_queries = (
            """
            DROP TABLE IF EXISTS clients CASCADE
            """,

            """
			DROP TABLE IF EXISTS drivers CASCADE
						""",

            """
            DROP TABLE IF EXISTS rideOffers CASCADE
            """,
            """
            DROP TABLE IF EXISTS rideRequests CASCADE
            """
        )
        for query in delete_queries:
            self.cursor.execute(query)
