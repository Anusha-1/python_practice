#single line function like this can be converted to lambda ... for small calculations , interest , exponentiation 
#def add5(x):
#    return x+5

add5= lambda x: x+5
print(add5(10))

#pure function /reusable function
def do_something(fn,val):
    #broker:logging ,profiling,caching,extra work
    print('LOGGED')
    return fn(val)

func =lambda x:x+1
print(func(10)) #11
print(do_something(func,5))
#print(do_something(dbconnectivity,"DB_RI")) --> like this different types of tasks

#keyword key is msut in sort 
list1 =[('eggs',5.35),('honey',9.5),('carrots',1.4)]
list1.sort(key =lambda x : x[1],reverse=True)
print(list1)

list2 =['a','d','c']
list2.sort()
print(list2)

#if else condition in lambda
starts_with_M= lambda x : True if x.startswith('M') else False
print(starts_with_M('anusha'))

