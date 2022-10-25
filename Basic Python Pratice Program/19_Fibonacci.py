def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))





while(1):
    N = int(input("enter an integer: "))
    if N == -1:
        break

    print( Fibonacci(N))
