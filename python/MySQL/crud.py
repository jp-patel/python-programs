# how to create a table
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jal11",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# how to check table that exist
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
print()


# how to create a table with primary key
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# how to insert record into table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jal", "Ahmedabad")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
print()


# how to insert multiple records into table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Jal', 'Ahmedabad'),
  ('Raj', 'Gandhinagar'),
  ('Sagar', 'Baroda'),
  ('Darpan', 'Mumbai'),
  ('Darshan', 'Surat'),
  ('Random', 'Random'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
print()


# how to get the id of last inserted record
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jal", "Ahmedabad")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
print()


# how to select record from table
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()


# how to select only desired column from table
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()


# how to select a particular record(s) from table
sql = "SELECT * FROM customers WHERE address ='Ahmedabad'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()


# how to sort the result
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()


# how to sort the result in descending order
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()


# how to delete record from table
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
print()


# how to drop a table
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)


# how to update value(s) of record(s)
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
print()


# how to get only required number of records
mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()
