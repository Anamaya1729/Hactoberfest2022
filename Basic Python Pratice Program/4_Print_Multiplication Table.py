""" This is a python program to print multiplication table of a number """

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def main():
    num = int(input("Enter a number: "))
    multiplication_table(num)

if __name__ == "__main__":
    main()
    
""" Multiplication table """
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
count = 1    

print ("The Multiplication Table of: ", number)    
while count <= 10:    
    number = number * 1    
    print (number, 'x', i, '=', number * count)    
    count += 1    
