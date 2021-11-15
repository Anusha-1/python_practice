#calc module:
def add(x,y):
    '''Add function expects 2 params and return sum'''
    return x+y

def divide(x,y):
    ''' divide fucntion expects 2 params and returns divison'''
    if y==0:
        raise ValueError('can not divide by zero')
    return x/y
