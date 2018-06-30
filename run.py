from app import app
from app.db import dbManager

dbUtils = dbManager.DBConnection()

if __name__ == "__main__":
	#dbUtils.create_tables()
	app.run(debug=True)
