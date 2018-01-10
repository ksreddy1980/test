

with open('corrept_file.txt') as fh:
    counter = 0
    counter1= 0
    for line in fh:
        for character in line:
            if character.isupper():
                counter = counter + 1
            elif character.isspace():
                counter1 = counter1 + 1



print counter
print counter1

