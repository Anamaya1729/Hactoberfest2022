
def fact_iterative(n):
    facto=1
    if(n==0):
        # print("Factorial of 0 is 1")
        return 1
    else:
        for i in range(1,n+1):
            facto=facto*i
        return facto
        # print("Factorial of ",n," is :",facto )
        
def fact_recursive(n):
    
    if(n==0):
        # print("Factorial of 0 is 1")
        return 1
    else:
         
        return n*fact_recursive(n-1)
        # print("Factorial of ",n," is :",facto )

print(fact_iterative(3))
print(fact_iterative(3))


