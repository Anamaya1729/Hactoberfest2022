X=[]
n=int(input("Enter N for N x N matrix : "))
print("Enter the element ::>")
for i in range(n): 
   row=[]                                       
for j in range(n): 
   row.append(int(input()))                
X.append(row)                           
print(X)
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(X[i][j], end=" ")                  
   print() 
Y=[]
n=int(input("Enter N for N x N matrix : "))    
print("Enter the element ::>")
for i in range(n): 
   row=[]                                      
   for j in range(n): 
      row.append(int(input()))           
   Y.append(row)                       
print(Y)
print("Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(Y[i][j], end=" ")
   print()                                            
result = [[0,0,0], [0,0,0], [0,0,0]] 
# iterate through rows 
for i in range(n):    
    for j in range(len(X[0])): 
        result[i][j] = X[i][j] + Y[i][j] 
        print("Result Matrix is ::>")
for r in result: 
   print("Result Matrix is ::>",r)
