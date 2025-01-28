def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Welcome to the Arithmetic Operations Program!")
    while True:
        operation = input("Choose an operation (add, subtract, multiply, divide) or 'exit' to quit: ").strip().lower()
        if operation == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if operation in ['add', 'subtract', 'multiply', 'divide']:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if operation == 'add':
                result = add(a, b)
            elif operation == 'subtract':
                result = subtract(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'divide':
                result = divide(a, b)
            
            print(f"The result of {operation}ing {a} and {b} is: {result}")
        else:
            print("Invalid operation. Please choose again.")


if __name__ == "__main__":
    main()