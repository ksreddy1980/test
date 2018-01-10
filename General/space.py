#
#
# str = 'jasfjh jfjkf jy  l mjj kjhjjgj h  jjjj'
# c= 0
# s =""
# for a in str:
#     if(a.isspace()):
#         c= c+1
#     else:
#         s = s + a
#
# print(c)
# l = str.split(" ")
# print(l)
# j = "".join(l)
#
# print(j)
#
#
# print(s)

l1 = [1,3,5]
l2 = [2,4,6,9,5]
# r = reduce(lambda x,y: x+y, l2)
# print(r)

def square(x):
    return x*x

l = map(square,l2)

print(l)

f = filter(lambda x: x % 2 ==0, l2)

print f

