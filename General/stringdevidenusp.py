
str = "ghsdfjkjkl1.@478 hdfjkl68"
s1 = ""
s2= ""
s3 = ""
n = len(str)
for a in str:
    if(a.isalpha()):
        s1 = s1 + a
    else:
        if (a.isdigit()):
            s2 = s2 + a
        else:
            s3 = s3 + a

print(s1)
print(s2)
print(s3)


