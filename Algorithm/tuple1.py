n  =  int(input("Enter the integer value:"))
l = []
l1 = []
x = 0
for i in range(1,(n/10)+1):
    x = x + 10
    l1.append(x)
    l.append(tuple(l1))

print(l)
print(l)




