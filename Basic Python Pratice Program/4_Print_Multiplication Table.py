""" This is a python program to print multiplication table of a number """

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def main():
    num = int(input("Enter a number: "))
    multiplication_table(num)

if __name__ == "__main__":
    main()