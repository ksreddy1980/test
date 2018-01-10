
n = int(input("enter the  value:"))

if(n <=0):
    n = int(input("enter the  value that greater than Zero:"))

def fib(n):
    first = 1
    second = 1
    if(n <=2):
        return 1
    else:
        for i in range(n-2):
            current = first + second
            first = second
            second = current
    return current

print("{0} Fibnoic number is {1}".format(n , fib(n)))





