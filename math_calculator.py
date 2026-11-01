import math

while True:
    print("\n===== MATHEMATICS CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quadratic Equation")
    print("6. Exit")

    choice = input("Select an operation (1-6): ")

    if choice == "1":
        print("\n--- ADDITION ---")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Answer:", result)

    elif choice == "2":
        print("\n--- SUBTRACTION ---")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Answer:", result)

    elif choice == "3":
        print("\n--- MULTIPLICATION ---")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Answer:", result)

    elif choice == "4":
        print("\n--- DIVISION ---")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Answer:", result)

    elif choice == "5":
        print("\n--- QUADRATIC EQUATION ---")
        print("Equation: ax² + bx + c = 0")

        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        if a == 0:
            print("Error: This is not a quadratic equation.")
        else:
            discriminant = b**2 - 4*a*c

            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)

                print("First root:", root1)
                print("Second root:", root2)

            elif discriminant == 0:
                root = -b / (2*a)
                print("Both roots are equal:", root)

            else:
                print("There are no real roots.")

    elif choice == "6":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid selection. Please choose between 1 and 6.")