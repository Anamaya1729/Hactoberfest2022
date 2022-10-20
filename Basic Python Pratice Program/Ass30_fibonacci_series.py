#fibonacci series using iteration
n=int(input("Enter upper bound "))
a=1
b=1
print("fibonacci series ",a,b,end=" ")
for i in range(3,n+1):
    p=a+b
    a=b
    b=p
    print(b,end=" ")
