

str = "ABC"

str = sorted(str)
l = len(str)

data = [""] * (l)

def stre(st,data,last,index):

    l = len(st)
    for i in range(l):
        data[index] = st[i]
        if index == last :
            print(data)
        else:
            stre(st,data,last,index+1)

stre(str,data,l-1,0)