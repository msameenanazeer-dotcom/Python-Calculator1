# Python Calculator
# A simple calculator for addition, subtraction, multiplication, and division

def calculator():
    print("===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1-4): "))

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
            print("Result:", result)

        elif choice == 2:
            result = num1 - num2
            print("Result:", result)

        elif choice == 3:
            result = num1 * num2
            print("Result:", result)

        elif choice == 4:
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result:", result)

        else:
            print("Invalid choice. Please select 1-4.")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
