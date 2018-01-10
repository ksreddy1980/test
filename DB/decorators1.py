

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed this before {0} ".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name,age):
    print('display_info function executedwith arguments {0} {1}').format(name, age)

display()

display_info('Aadvik',2)


