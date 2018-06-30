import psycopg2
import psycopg2.extras as extra
from pprint import pprint


class DBConnection:
	def __init__(self):
		try:
			self.con = psycopg2.connect(database="farooq", user="postgres", password="", host="localhost",
			                            port="5432")
			self.con.autocommit = True
			self.cursor = self.con.cursor()
			self.dict_cursor = self.con.cursor(cursor_factory=extra.DictCursor)
		except Exception as ex:
			pprint(ex)

	def create_tables(self) -> object:
		"""

        :rtype: object
        """
		print("I am here")
		# status pending,approved, rejected
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
            CREATE TABLE IF NOT EXISTS requests (
                request_id SERIAL PRIMARY KEY,
                ride_id INTEGER NOT NULL,
                client_id INTEGER NOT NULL,
                FOREIGN KEY (ride_id)
                    REFERENCES rideOffers (ride_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (client_id)
                    REFERENCES clients (client_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                status VARCHAR(10) NOT NULL
            )
            """
		)
		for query in queries:
			self.cursor.execute(query)


if __name__ == "__main__":
	db = DBConnection()
	db.create_tables()
