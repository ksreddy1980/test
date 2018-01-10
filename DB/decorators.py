
def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print("Not in in the original function")
            return original_function(*args, **kwargs)
        return wrapper_function

@decorator_function
def display():
    print("Display function ran")

@decorator_function
def display_info(name,age):
    print("Display info function ran with arguments: ({0}, {1})".format(name,age))


display()

display_info('Aadvik',2)