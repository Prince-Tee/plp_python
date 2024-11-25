#Basic Calculator
num1 = float(input("Enter the first number: " ))
num2 = float(input("Enter the second number: " ))
operation = (input("enter the operation (+, -, *, /): "))

if operation == "+":
    print(f'{num1} + {num2} = {num1 + num2}')
elif operation == "-":
    print(f'{num1} - {num2} = {num1 - num2}')
elif operation == "*":
    print(f'{num1} * {num2} = {num1 * num2}')    
elif operation == "/":
    print(f'{num1} / {num2} = {num1 / num2}')  
else:
    print("not a valid operation")      