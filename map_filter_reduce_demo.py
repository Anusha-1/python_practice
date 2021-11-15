
"""
map,filter,reduce are paradigms of FUNCTIONAL programming
they allow u to write ----> simpler , shorter code w/o bother about intricacies like loops and branching
this is same as javascript

this is useful for ml, data analytics ,business analytics

map(func,*iterables) iterable --iterable: list , set or collection  which can be interated , not on dict it will work

"""
names =['anusha','chaitanya','a','c']
uppered_names=[]
#for n in names:
#    name_=n.upper()
#    uppered_names.append(name_)
uppered_names = list(map(str.upper(),names))


#we can pass lambda/non lambda functions  to map
numbers=[1,2,3,4,5]
squared =map(lambda num : num**2, numbers)
print(type(squared))
print(list(squared))

#example for non lambda functions to map
def CToF(cels):
    return 9/5*cels+32

def FToC(fahr):
    return (fahr-32)*5/9

ct=[45,34,23]

print(list(map(CToF,ct)))

ft=[212,134,123]
print(list(map(FToC,ft)))


##############filter data analysis /BL /DL##################
scores=[99,66,87,90,99,88,55,67,6,45,56,34,33]
def is_a_score(score):
    return score>75

over_75 =list(filter(is_a_score,scores))
print(type(over_75))
print(over_75)

# pass lambda functions to filter
mylist=[1,8,7,13,20,6]
new_list=filter(lambda x: x%2==1, mylist)
print(list(new_list))


##############reduce ##################
from functools import reduce
numbers =[3,4,6,9,34,12]

def custom_sum(first,second):
    return first+second

result =reduce(custom_sum,numbers)
print(result)

####real time
import functools,operator,os,os.path
files=os.listdir(os.path.expanduser("."))
print(functools.reduce(operator.add,map(os.path.getsize,files)))

###########numpy demo
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
squarer=lambda t :t**2
squares=np.array([squarer(xi) for xi in x])
print(type(squares))
print(squares)
