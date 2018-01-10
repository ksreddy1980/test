l = list(input("enter the list of elements:"))

def largest(l):
    n = len(l)
    max = 0
    max2 = 0
    for i in range(n):
        if (max < int(l[i])) :
            max = int(l[i])
        if (int(l[i])> max2 and int(l[i]) < max):
            max2 = int(l[i])
    return max2

print("largest number in the given list is : {}".format(largest(l)))

