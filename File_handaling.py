#requirements
import numpy as np
import pandas as pd
import mysql.connector as mysql

database = mysql.connect(
	host="localhost",
	user="root",
	password="vishal2003"

),
database.autocommit = True	#connect to the database
cursor = database.cursor()					
# Create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS file_handling_db")	
# Use the database
cursor.execute("USE file_handling_db")
# Create a table	
cursor.execute("CREATE TABLE IF NOT EXISTS file_handling_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
# Insert data into the table
cursor.execute("INSERT INTO file_handling_table (name, age) VALUES ('John Doe', 30)")
cursor.execute("INSERT INTO file_handling_table (name, age) VALUES ('Jane Smith', 25)")			
# Commit the changes
database.commit()

# File handling in Python




	




print("Learning Python file handling...")
# This is a simple Python script to demonstrate file handling
def Load_the_file(m):
	f=open(m, "r")
	print("File opened successfully.")
	print(f.read(25)) #read 25 the id charcters from the file
	print(type(f))

	f.close()
	print("File closed successfully.")


#performing other operations

def Perform_operation_on_load_file(m):
	f=open(m, "r")
	print("File opened successfully.")
	print(f.read(25)) #read 25 the id charcters from the file
	print(type(f))
	print(f.name) #print the name of the file	
	print(f.mode) #print the mode of the file

	f.close()
	print("File closed successfully.")
Perform_operation_on_load_file("list2.csv")

