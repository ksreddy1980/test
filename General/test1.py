a = [-1,100,2,9,3,6,29,14,68,24,29,99,72,4,0]

n = len(a)

for i in range(1, n):
    key = a[i]
    j = i-1
    while(j >= 0) and (a[j] > key):
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = key


print(a)