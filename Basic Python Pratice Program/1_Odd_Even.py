""" This is a python program to check if a number is odd or even """

def odd_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

def main():
    num = int(input("Enter a number: "))
    odd_even(num)

if __name__ == "__main__":
    main()