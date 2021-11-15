#decorator is behavioural design pattern
'''
Attach additional responsibilities at run time 
for loosely coupled architecture with extensibility / resusability

decorators=functions
logging, profiling, security check, cache, ...


'''

def say_hello(name):
    return f"Hello {name}!"

def appreciate(name):
    return f"Yo {name}, you are great! "

#decorator
def greet(fnptr):
    "''logging/tracing/profiling .... ''"
    print("logging here")
    return fnptr("Anusha")

print(greet(say_hello))
print(greet(appreciate))


#logger decorater
def logger(func):
    def wrapper():
        print("I am logging data in db")
        func()
        print("I am logging after calling the function in db")
    return wrapper

@logger
def invoke():
    print("Anusha")

invoke()
