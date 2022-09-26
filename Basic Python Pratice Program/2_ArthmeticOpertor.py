""" This is a python program to perform arithmetic operations """

def arithmetic(num1, num2):
    print(f"Addition: {num1 + num2}") # Addition
    print(f"Subtraction: {num1 - num2}") # Subtraction
    print(f"Multiplication: {num1 * num2}") # Multiplication
    print(f"Division: {num1 / num2}") # Division
    print(f"Floor Division: {num1 // num2}") # Floor Division
    print(f"Exponent: {num1 ** num2}") # Exponent
    print(f"Modulus: {num1 % num2}") # Modulus

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    arithmetic(num1, num2)

if __name__ == "__main__":
    main()