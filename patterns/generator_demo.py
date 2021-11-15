#generators
'''
generator functions are spl. types that iterate only once

why?
generator saves lots of memory and improves performance
as it generates the values/data on fly(on demand)

yield -keyword instead of return

diff between normal for loop and generator

iterators will save values in memory, generators dont
'''


#def square_numbers(nums):
#    result=[]
#    for i in nums:
#        result.append(i*i)
#    return result

def square_numbers(nums):
    for i in nums:
        yield i*i
    

my_nums =square_numbers([1,2,3,4,5]) 
print(type(my_nums)) #class generator
print(my_nums) #generator object
print(next(my_nums)) #1
print(next(my_nums)) #4


#profiling the generator and iterator
def topfive():
    n=1
    while n<=5:
        sq=n*n
        yield sq
        n+=1
    
values=topfive()
print(type(values))
for i in values:
    print(i)

alist=['Python','Java','C++','Ruby']

def list_items():
    for item in alist:
        yield item

gen =list_items()
iter=0
while iter<len(alist):
    print(next(gen))
    iter+=1
print(iter)

for items in gen:
    print(items)
