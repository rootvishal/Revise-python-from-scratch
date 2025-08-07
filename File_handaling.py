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

