fibonacciSeries = [0,1]
n = int(input("Input the number of elements in fibonacci series - "))
def fibSer(n):
    if n<0:
        return "error"
    elif n>1:
        i = 2
        while n != i:
            fibonacciSeries.append(fibonacciSeries[i-1] + fibonacciSeries[i-2])
            i += 1
fibSer(10)
print(f"First {n} members of fibonacci series are : ", fibonacciSeries)