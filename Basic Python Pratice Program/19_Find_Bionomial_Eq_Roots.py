def smaller(a,b):
    if a>b:
        return b
    else:
        return a


print("ax^2 + bx + c = 0")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

ac = a*c
ls = []

# To find two no. that may can split
for i in range((ac//2)+1):
    for j in range((ac//2)+1):
        temp = i*j
        if temp == ac:
            ls.append([i,j])
print(ls)


# To check they can be fit in condition
ls1 = []
for i in ls:
    if i[0]+i[1] == b:
        ls1.append(i)
    if i[0]-i[1] == b:
        ls1.append([i[0],-i[1]])
print(ls1)


# To find value of common element
y = smaller(a, ls1[0][0])
z = smaller(c, ls1[0][1])

same = ls1[0][0]//a
print(y, z, same)

# try a lame method to find x
if a < ls1[0][0]:
    same = ls1[0][0]//a
else:
    same = a//ls1[0][0]

print(f"Value of x by lame method is {-same}")
