import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='3052'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")