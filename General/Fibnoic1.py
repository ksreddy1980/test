n = int(input("enter the  value:"))

if(n <=0):
    n = int(input("enter the  value that greater than Zero:"))

def fib(n):
    if ((n == 1) or (n == 0)):
        return 1
    else:
        return (fib(n-1)+fib(n-2))

print("{0} Fibnoic number is {1}".format(n , fib(n-1)))