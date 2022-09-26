""" This is a program to calculate the factorial of a number using a for loop and a while loop. """

def factorial_for(n):
    """ This function calculates the factorial of a number using a for loop. """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_while(n):
    """ This function calculates the factorial of a number using a while loop. """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    """ This is the main function. """
    print(f"factorial_for(5) = {factorial_for(5)}")
    print(f"factorial_while(5) = {factorial_while(5)}") 

if __name__ == "__main__":
    main()