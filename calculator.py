# calculator.py
import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <num1> <num2> <operation>")
        print("Operation: add, subtract, multiply, divide")
        sys.exit(1)

    # Read input from command-line arguments
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Please enter valid numbers.")
        sys.exit(1)

    operation = sys.argv[3].lower()

    # Perform operation
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        print("Invalid operation! Choose add, subtract, multiply, divide.")
        sys.exit(1)

    print(f"Result: {result}")
    print("Update")
    print("second update")
