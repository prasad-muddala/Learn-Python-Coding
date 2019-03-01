#addition
def add(m,n):
	return m+n
# subtraction
def sub(m,n):
	return m-n
#multiplication
def mul(m,n):
	return m*n
##division
def div(m,n):
	return m/n

print(""" Select the operation you want to perform
	1.Addition
	2.Subtraction
	3.Multiplication
	4.Division
	""")
print("enter two values to perform the operation")
num1=int(input())
num2=int(input())
choice=int(input("enter your choice "))

if choice==1:
	print("result is: "+str(add(num1,num2)))
elif choice==2:
	print("result is: "+str(sub(num1,num2)))
elif choice==3:
	print("result is: "+str(mul(num1,num2)))
elif choice==4:
	print("result is: "+str(div(num1,num2)))
else:
	print("wrong choice you")
