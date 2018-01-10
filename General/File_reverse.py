

with open('corrept_file.txt') as fh:
  with open('re.txt',"w") as fp:
    for line in fh:
        l = 0
        l = len(line)
        for i in range(1,l+1):
            fp.write(line[l-i])
        fp.write("\n")





