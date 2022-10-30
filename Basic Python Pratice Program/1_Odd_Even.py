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
""" Odd or even program """
def evenOdd(n):
     
    #if remainder is 0 then num is even
    if(n==0):
        return True
       
    #if remainder is 1 then num is odd
    elif(n==1):
        return False
    else:
        return evenOdd(n-2)
       

num=int(input())
if(evenOdd(num)):
    print(num,"num is even")
else:
    print(num,"num is odd")
