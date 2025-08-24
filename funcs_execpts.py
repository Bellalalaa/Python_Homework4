#!/usr/bin/python3


def Get_age():
	while True:
		try:
			age = int(input("Please enter your age"))
		except ValueError:
			print("No,Proper number please")
		else:
			break
	return age

people_list = []
endVerification = False
while not endVerification:
	fname = input("Enter your name")
	variable_is_int = True
	age = Get_age()
	verif_dict = {"Name" : fname,"age" :age}
	people_list.append(verif_dict)
	endVerification = input("to finish verification print f  ")
	if endVerification.lower == "f":
		break

print(people_list)


	
