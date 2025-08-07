print("Learning Python file handling...")
# This is a simple Python script to demonstrate file handling
def Load_the_file(m):
	f=open(m, "r")
	print("File opened successfully.")
	print(f.read(25)) #read 25 the id charcters from the file
	print(type(f))

	f.close()
	print("File closed successfully.")
Load_the_file("list2.csv")

