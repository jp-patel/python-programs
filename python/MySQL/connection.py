import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jal11"
)

mycursor = mydb.cursor()

# how to create database
mycursor.execute("CREATE DATABASE mydatabase")

# how check databases that already exist
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
print()

# how to connect to a database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jal11",
  database="mydatabase"
)

print(mydb)
print()