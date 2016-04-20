# Basic Calculator
import math

def add(*args):
    total = 0
    for i in args:
        total += i
	
def subtract(x, y):
	return x - y 
	
def multiply(x, y):
	return x * y 
	
def division(x, y):
	return x / y 
	
def expo(x, y):
	return pow(x, y)
	
def squareroot(x):
	return math.sqrt(x)
	
def sin(x):
	return math.sin(x)
	
def tan(x):
	return math.tan(x)
		
def cos(x):
	return math.cos(x)

	
# take input from user
print("Select option")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
print("5.expo")
print("6.squareroot")
print("7.sin")
print("8.tan")
print("9.cos")

choice = input("Enter your choice: " )

# x = num1
# y = num2

num1 = float(input("Enter first number: " ))
num2 = float(input("Enter second number: " ))

if choice == '1':
	print(num1, '+', num2, '=', add(num1, num2))
elif choice == '2':
	print(num1, '-', num2, '=', subtract(num1, num2))
elif choice == '3':
	print(num1, '*', num2, '=', multiply(num1, num2))
elif choice == '4':
	print(num1, '/', num2, '=', division(num1, num2))
elif choice == '5':
	print(expo(num1, num2))
elif choice == '6':
	print('squareroot of', num1, '=', squareroot(num1))
elif choice == '7':
	print(sin(num1))
elif choice == '8':
	print(tan(num1))
elif choice == '9':
	print(cos(num1))
else:
	print("You have entered an invalid option")
	
input("Press <Enter>")
