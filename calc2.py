import Additon
import Subtraction
import multiply
import divide

while True:
    print("\n--- Proper Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select an operation (1-4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            print(f"Result: {add.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide.divide(num1, num2)}")
    else:
        print("Invalid selection. Try again.")
