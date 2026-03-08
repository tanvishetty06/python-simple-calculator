print("Simple Calculator")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", a + b)

elif operation == "-":
    print("Result:", a - b)

elif operation == "*":
    print("Result:", a * b)

elif operation == "/":
    print("Result:", a / b)

else:
    print("Invalid operation")
