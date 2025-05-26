import math

def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Logarithm")
        print("9. Trigonometric (sin, cos, tan)")
        print("10. Exit")

        choice = input("Choose operation (1-10): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

        elif choice == '4':
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero!")

        elif choice == '5':
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", math.pow(a, b))

        elif choice == '6':
            a = float(input("Enter number: "))
            if a >= 0:
                print("Result:", math.sqrt(a))
            else:
                print("Error: Negative number!")

        elif choice == '7':
            a = int(input("Enter number: "))
            if a >= 0:
                print("Result:", math.factorial(a))
            else:
                print("Error: Factorial of negative number!")

        elif choice == '8':
            a = float(input("Enter number: "))
            if a > 0:
                print("Natural log:", math.log(a))
                print("Base-10 log:", math.log10(a))
            else:
                print("Error: Log of non-positive number!")

        elif choice == '9':
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("sin:", math.sin(rad))
            print("cos:", math.cos(rad))
            print("tan:", math.tan(rad))

        elif choice == '10':
            print("Exiting calculator.")
            break

        else:
            print("Invalid choice. Please choose 1-10.")

calculator()
