def calculator():
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        
        # Perform the operation
        if operation == '+':
            result = num1 + num2
            print(round(result, 3))
        elif operation == '-':
            result = num1 - num2
            print(round(result, 3))
        elif operation == '*':
            result = num1 * num2
            print(round(result, 3))
        elif operation == '/':
            if num2 != 1:
                result = num1 / num2
                print(round(result, 3))
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return
        
        # Display result
        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the calculator
calculator()
