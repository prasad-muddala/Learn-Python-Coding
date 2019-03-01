Task 1:
----------------------------------------------------------------
solution:
#second highest in the list
if __name__=='__main__':
	n=int(input())
	arr=list(map(int,input().split()))
m=max(arr)
i=0
while i<n:
	if m==max(arr):
		arr.remove(m)
	i=i+1

print(max(arr))
----------------------------------------------------------------

Task 2:
----------------------------------------------------------------
solution:
#area of the triangle
def area(p,x,y,z):
	return ((p*(p-x)*(p-y)*(p-z))**0.5)

print(""" enter the values of the
	sides of the triangle to find the area
	""")
a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
result=area(s,a,b,c)

print("area of the triangle is "+str(result))

----------------------------------------------------------------

Task 3:
----------------------------------------------------------------
solution:
#armstrong number
def armstrong(n):
	sum=0
	m=n
	while m>0:
		digit=m%10
		sum=sum+digit**3
		m=m//10
	if sum==n:
		print("{} is an armstrong number".format(n))
	else:
		print("{} is not armstrong".format(n))
print("enter a value:")
val=int(input())
armstrong(val)

----------------------------------------------------------------

Task 4:
----------------------------------------------------------------
solution:
#decimal to binary
def Binary(n):
	if n>1:
		Binary(n//2)
	print(n%2,end="")
print("enter a decimal value to be converted")
a=int(input())
Binary(a)
----------------------------------------------------------------

Task 5:
----------------------------------------------------------------
solution:
#factorial using recursion
def factorial(n):
	if n==0:
		return 1
	elif n==1:
		return 1
	else:
		return n*factorial(n-1)

print("enter a value to find its factorial: ")
a=int(input())
result=factorial(a)
print("It's factorial value is "+str(result))
----------------------------------------------------------------

Task 6:
----------------------------------------------------------------
solution:
#LCM of two numbers
def Lcm(a,b):
	if a>b:
		lar=a
	else:
		lar=b
	while(True):
		if(((lar%a)==0) and ((lar%y)==0)):
			lcm=lar
			break
		lar+=1
	return lcm
x=int(input())
y=int(input())
val=Lcm(x,y)
print(val)
----------------------------------------------------------------

Task 7:
----------------------------------------------------------------
solution
#leap year
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0:
        leap=True
    elif year%100!=0 and year%4==0:
        leap=True
    else:
        leap=False
    
    return leap

year = int(input())
print(is_leap(year))
----------------------------------------------------------------

Task 8:
----------------------------------------------------------------
solution
#to check whether a number is prime or not
def prime(m):
	for i in range(2,m):
		if m%i==0:
			break
	else:
		print("entered value " + str(m) +"is prime")
val=int(input("enter a value "))
prime(val)
----------------------------------------------------------------

Task 9:
----------------------------------------------------------------
solution:
#finding the vowel count in then text
vowels="aeiou"
print("enter a string")
str=input()
str=str.casefold()
count={}.fromkeys(vowels,0)
for char in str:
	if char in vowels:
		count[char]+=1
print(count)
----------------------------------------------------------------

Task 10:
----------------------------------------------------------------
solution:
#roots of the quadratic equation
import cmath
print("enter the coefficients of the quadratic equation: ")
a=float(input())
b=float(input())
c=float(input())

d=(b**2)-(4*a*c)
sol1=((-b)+cmath.sqrt(d))/(2*a)
sol2=((-b)-cmath.sqrt(d))/(2*a)
print("solutions are {0},{1} " .format(sol1,sol2))
----------------------------------------------------------------
