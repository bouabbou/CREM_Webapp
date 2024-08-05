import mysql.connector

# Connect to the MySQL server
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2002'
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Create a new database
cursorObject.execute("CREATE DATABASE infrastructure")

print("All done")
