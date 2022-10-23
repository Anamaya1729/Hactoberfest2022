fibonacciSeries = [0,1]

def fibSer(n):
    if n<0:
        return "error"
    elif n>1:
        i = 2
        while n != i:
            fibonacciSeries.append(fibonacciSeries[i-1] + fibonacciSeries[i-2])
            i += 1
fibSer(5)
print(fibonacciSeries)