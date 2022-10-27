st = input("Enter a String: ")
lt = list(st.split(" "))
for x in reversed(lt):
    print(x, end=' ')
