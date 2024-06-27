def add(a, b):
    a = float (a)
    b = float (b)
    return a+b

def substraction(a, b):
    a = float(a)
    b = float (b)
    return a-b

def multiplication(a, b):
    a = float(a)
    b = float(b)
    return a*b

def divide(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        return "ERROR!, THIS NUMBER BE ONLY IN 0"
    return a/b

def exponent(a, b):
    a = float(a)
    b = float(b)
    return a**b

#main program
print("Welcome to calculator!")
print("----------------------------")
print("Please select an operation:")
print("1.Add")
print("2.Substraction")
print("3.Multiplication")
print("4.Divided")
print("5.Exponent")
print("6.Exit")
print("----------------------------")

#Second program
operation = input("Enter your choice (1/2/3/4/5): ")
if operation == '1':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '2':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1, "-", num2, "=", substraction(num1, num2))
elif operation == '3':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif operation == '4':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1, "/", num2, "=", divide(num1, num2))
elif operation =='5':
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    print(num1, "**", num2, "=", exponent(num1, num2))
elif operation == '6':
    print("Exiting...Thank you for using calculator")
else:
    print(" Fuck off! nahhh. PLease try again later u sucker ")
#python calculator.py