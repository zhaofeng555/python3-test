import time

def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name):
    print('this is a function')

@decorator
def f2(func_name1, func_name2):
    print('this is a function named1 ' + func_name1)
    print('this is a function named2 ' + func_name2)

f1('hello')
f2('hello', 'world')

