# Function to perform the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main calculator function
def calculator():
    print("Hello developer!!")
    print("Hi")
    print("Welcome to the Python Calculator!")
    print("Operations: +, -, *, /")

    # User input for operation choice
    operation = input("Enter the operation (+, -, *, /): ")

    # User input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    # Perform the chosen operation
    if operation == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation! Please choose from +, -, *, /.")

# Running the calculator
calculator()