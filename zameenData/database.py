import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="zameen"
)

print("MySQL connected successfully!")

connection.close()
