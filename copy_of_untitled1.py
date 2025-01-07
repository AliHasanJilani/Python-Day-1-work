# Python ---> Python is general - purpose , interpreted programming language which was invented in 1991 by guido van rassoum .
# For check version
# python --version

# Fundamentals of Python
# (1). variales
# (2). Data types
# (3). input(),print()

# (1). Variales ----> This is a container in which we will store values or assign .
a = 56
b = 'sam'
c = 76.8

### here a,b,c = variales.

# (a). Global variales ---> Entirely modify
# (b). local variales ---> specific block of code modify

# (2). Dta type ---->
# (a). Integer ---> All postive or negative values .
# Ex. 34 , 44 , -12

# (b). float ----> All decimal values
# Ex. 22.23 ,234.44

# (c). string ---> 'single_quotes' , "double_quotes" , '''triple_quotes'''
# Ex. 'sam' , "sam" , '''sam'''

# (d). boolean ----> true , false
# Ex. 5>4 ---> true

# type() ----> using type(), we can check data type .

type(33<50)

type('45.90')

# type casting ----> using type casting , we can convert or change values from one data type tp another data type .

a = 67
type(a)
b = float(a)
type(b)
b

# print() ---> it will execute our query on terminal .

a = 1
print(a)
print("first line completed")
b = 2
print(b)

# input() ---> This is a pre-defined function of python . it will take query from user and send it to the function .
# And its output will be string format by default .

a = 1
b = 2
c = a + b
print(c)

a = '1'
b = '2'
c = a + b
c

a = input("Enter first number:")
b = input("Enter second number:")
c = a + b
print(c)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = a + b
print(c)

#commonly use operators
# (1). Add(+)--->5+3 = 8
# (2). subtraction(-)--->5-3 = 2
# (3). multiplication(*)--->2*4 =8
# (4). Division (/)---> 5/2=2.5
# (5). floor division(//) --> 5//2 = 2
# (6). module(%)---> for remainder calculations---> 25%10=5(remainder)
# (7). Equal to(=)---> for value assignment ---> a=5 , b='sam'
# (8). Equal equal to (==) For values comparison --> a == 5 , 'sam' == 'mohit'
# (9). not equal to (!=)
# (10). Greater than (>)---> 5>4
# (11). Greater than or equal to (>=) --->5>=5
# (12). less than (<)
# (13). less tha or equal to (<=)

# conditional statement in python

# (1). if
# (2). elif       -user
# (3). else

# Ex.1

a = input("Enter your name :")
if(a=="sam"):
 print("yes")
elif(a=="rahul"):
  print("no")
elif(a=="mohit"):
  print("ok")
else:
  print("Please enter a valid name....")

# Ex. 2

print("we provide these items : pizza , burger , icecream , sandwish")
print("pizza:120 , burger:70 , icecream:50 , sandwish:90")

a = input("Enter your item :")
if(a=="pizza"):
  print("Pizza is available")
  b = int(input("Please tell me how many pizza you want:"))
  c = b*120
  if(1000>2000):
    print("your actual price is:",c)
    print("your 10% discounted price is:", c-(c*0.1))
  elif(c>=2000):
    print("your actual price is:",c)
    print("your 20% discounted price is:", c-(c*0.2))
  elif(c<1000):
    print("your actual price is:",c)
    print("your total cost is:",c)
elif(a=="burger"):
  print("burger is available")
  b = int(input("Please tell me how many burger you want:"))
  c = b*70
  if(1000>2000):
    print("your actual price is:",c)
    print("your 10% discounted price is:", c-(c*0.1))
  elif(c>=2000):
    print("your actual price is:",c)
    print("your 20% discounted price is:", c-(c*0.2))
  elif(c<1000):
    print("your actual price is:",c)
    print("your total cost is:",c)
elif(a=="icecream"):
  print("icecream is available")
elif(a=="sandwish"):
  print("sandwish is available")
else:
  print("please enter a vaild item .... ")

print("we provide these cources: python , java , mern")

a=input("Enter your course:")

if(a=="python"):
  print("python is available\nDuration:4 Months\nfees:5000")
elif(a=="java"):
  print("java is available\nDuration:3 Months\nfees:3000")
elif(a=="mern"):
  print("mern is available\nDuration:2 Months\nfees:2000")
else:
  print("Enter a vaild course")

# loop in python ---->
# (1). For loop
# (2). while loop

# (1). For loop

# index = 0 , length = 1
# starting values will include and last value will exclude .

# method - 1
for i in range(1,5):
  print(i)

for i in range(1,10,2):
  print(i)

for i in range(3):
  for j in range(2):
    print(f"i={i} , j={j}")

n = 5
for i in range(1,n+1):
  print("*" * i)

n = 5
for i in range(1,n+1):
  if i==1 or i==n:
    print("*" * i)
  else:
    print("*" + " " * (i-2) + "*")

n = 5
for i in range(1,n+1):
  print(' ' * (n-i) + '*' * (2*i-1))

# (2). while loop

# (a). Initialization
# (b). condition
# (c). Increment or decrement

# Q.1 Write a program who print from 1 to 4

i = 1
n = 4
while(i<=n):
  print(i)
  i=i+1

i = int(input("Enter first number: "))
n = int(input("Enter last number: "))
while(i<=n):
  print(i)
  i=i+1

i = 5
n = 1
while(i>=n):
  print(i)
  i=i-1

i = 1
n = 5
sum = 0
while(i<=n):
  sum = sum + i
  i = 1+i
print(sum)

#take a variable if that variable is 2 a multiply  6  than print 'hy'

Age = int(input("Enter your age:"))

if(Age<=10):
  print("child")
elif(Age<=18):
  print("adult")
elif(Age<=30):
  print("mature")
elif(Age<=60):
  print("old")
else:
  print("new born")

age = int(input("Enter a number :"))

if(age>5):
  print("Aadhar card created")
  if(age>18):
    print("Aadhar and Pan card is linked")
  else:
     print("PAN CARD NOT CREATED")
else:
  print("Age is small")

i = int(input("Enter a number:"))
if(i%2==0):
  print("even")
else:
  print("odd")

a = int(input("Enter first number:"))
b = int(input("Enter secound number:"))
c = int(input("Enter third number:"))

if(a>b and a>c):
  print("a is greater")
elif(b>a and b>c):
  print("b is greater")
elif(c>a and c>b):
  print("c is greater")
else:
  print("Enter a vaild numbers")

year = int(input("Enter a year:"))
if(year%4==0 and year%100!=0 or year%400==0):
  print("leap year")
else:
  print("not a leap year")

percentage = int(input("Enter a percentage:"))
if(percentage>=90):
  print("Grade A")
elif(percentage>=80):
  print("Grade B")
elif(percentage>=70):
  print("Grade C")
elif(percentage>=60):
  print("Grade D")
elif(percentage<60):
  print("Grade F")

letter = input("Enter a letter:")
if(letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u"):
  print("vowel")
else:
  print("consonant")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
operator = input("Enter a operator:")
if(operator=='+'):
  print(num1+num2)
elif(operator=='-'):
  print(num1-num2)
elif(operator=='*'):
  print(num1*num2)
elif(operator=='/'):
  print(num1/num2)

number = int(input("Enter a number:"))

if(number>0):
  print("positive")
elif(number<0):
  print("negative")
else:
  print("zero")

username = input("Enter a username:")
password = input("Enter a password:")
if(username=="admin" and password=="1234"):
  print("login successful")
else:
  print("login failed")

age = int(input("Enter your age:"))

if(age<=1):
  print("infant")
elif(age<=4):
  print("Toddler")
elif(age<=12):
  print("child")
elif(age<=19):
  print("Teenager")
elif(age<=59):
  print("Adult")
else:
  print("senior")

A = int(input("Enter first side:"))
B = int(input("Enter secound side:"))
C = int(input("Enter third side:"))

if('A+B>C' and 'B+C>A' and 'C+A>B'):
  print("vaild triangle")
else:
  print("invaild triangle")

