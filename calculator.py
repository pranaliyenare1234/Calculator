# Simple Calculator in Python

def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation.")
        return

    # Display result
    print(f"Result: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
