def decorator_function(func):
    def wrapper():
        print('Start decorate function: {}'.format(func.__name__))
        func()
        print('End decorate')
    return wrapper

def decorator_with_args(s):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(s)
            func(s)
            return s
        return wrapper()
    return actual_decorator

@decorator_function
def hw():
    print('Hello World!')

@decorator_with_args('Skillfactory')
def hw2(s):
    print('Hello World, {}!'.format(s))

if __name__ == '__main__':
    hw()
    hw2()