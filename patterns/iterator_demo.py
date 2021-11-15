nums=[1,4,2,3]
print(nums[1])
for i in nums:
    print(i)

it= iter(nums)
print(type(it)) #<class list-iterator>

print(it.__next__()) #1
print(it.__next__()) #4
print(next(it)) #2
print(next(it)) #3
print(next(it))  #exception stopiteration


#custom iterator
#pd.head(10) pd.tail() paginator
class Head:
    def __init__(self,max=5):
        self.num=1
        self.max=max
    
    def __iter__(self):
        return self

    def __next__(self):
        """ write custom logic to return data with pagination"""
        if self.num <= self.ax:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values=Head(10)
for i in values:
    print(i)
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())


