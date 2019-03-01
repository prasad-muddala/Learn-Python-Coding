
"""this is my solution if you came up with something different let me know i will add it mentioning your name"""

#birthday database
Birthdays={'Ram':'jan 2','Sandhya':'jan 12','Swamy':'mar 12','Dad':'dec 15'}
while True:
	print("enter the name of the student to know their birthdate:(blank to exit)")
	name=input()
	if name=="":
		break

	if name in Birthdays:
		print(Birthdays[name]+" is the bithday of "+ name)
	else:
		print("we dont have any  details about that student")
		print("please enter the birthdate of "+name)
		bday=input()
		Birthdays[name]=bday
		print("now we have updated our database")
		print("""-----Thank You-----""")
