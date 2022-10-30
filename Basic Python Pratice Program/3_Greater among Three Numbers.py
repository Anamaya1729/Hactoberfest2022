""" This is a python program to find the greatest among three numbers """

def greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))
    greatest(num1, num2, num3)

if __name__ == "__main__":
    main()
    
""" greatest among three numbers"""

num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

