def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        raise ValueError("Invalid operator. Please use +, -, *, or /.")

try:
    # Step 4: Prompt the user to enter two numbers and convert them to floats
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Step 5: Prompt the user to enter an arithmetic operation
    op = input("Enter an arithmetic operation (+, -, *, /): ")

    # Step 6: Call the function with the numbers and the operation
    result = calculate(num1, num2, op)

    # Step 7: Print the result of the operation
    print(f"The result of {num1} {op} {num2} is: {result}")

except ValueError as ve:
    # Step 8a: Handle ValueError
    print(f"ValueError: {ve}")

except ZeroDivisionError as zde:
    # Step 8b: Handle ZeroDivisionError
    print(f"ZeroDivisionError: {zde}")

except Exception as e:
    # Step 8c: Handle any other exceptions
    print(f"An unexpected error occurred: {e}")

finally:
    # Step 9: Print end-of-program message
    print("Program has ended.")

