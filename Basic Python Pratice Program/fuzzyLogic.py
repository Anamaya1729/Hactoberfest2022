#program for FUZZY LOGIC
A = dict()
B= dict()
Y= dict()

A = {"a":0.8, "b":0.1, "c":0.4, "d":0.3}
B = {"a":0.9, "b":0.6, "c":0.4, "d":0.1}

print("Fuzzy set of A", A)
print("Fuzzy set of B", B)

for A_key, B_key in zip(A,B):
    A_value = A[A_key]
    B_value = B[B_key]

    if (A_value > B_value):
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value

print("Fuzzy set union is", Y)
