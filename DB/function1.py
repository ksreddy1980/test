#First class functions

def square(x):
    return x * x
def cube(x):
    return x * x* x

f1 =  square   # Assigning function to a variable
f2 = cube

# print(f1(2))
# print(f2(2))

# passing function as an Argument

def my_map(func,l):
    result = []
    for i in l:
        result.append(func(i))
    return result

# print(my_map(square, [2,3,1,4,6,10]))
#
# print(my_map(cube, [2,3,1,4,6,10]))

#Function returning a function

# def display(msg):
#     def inner():
#         print(msg)
#     return inner
# hello = display("Hi I am variable in thr scope of outer function")
# print(hello())

#Another program for returning a function

def html_tag(tag):
    def wrap_text(msg):
        print("<{0}> <{1}> </{0}>").format(tag,msg,tag)
    return wrap_text

h = html_tag('h1')

h("this is the first text need to be wraped in h1 header")
h("this is the second text need to be wraped in h1 header")

p = html_tag('p')

p('this is a paragraph one')
p('this is a paragraph two')




