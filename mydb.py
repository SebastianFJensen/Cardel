import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Cardelejendomme23!?!'
	)

#prepare curser object

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE Cardel")

print ("ALL done!") 