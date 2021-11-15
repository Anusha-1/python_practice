##private object in python class : __ ( 2 underscores) , __age ,__name : these are all private variables


class Student(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        self.city='HYDERABAD'

    def getAge(self):
        return self.__age

    
if __name__ =='__main__':
    s=Student('Anusha',23)
    #print(f"NAME{s.__name}")
    print(f"age {s.getAge()}")
    print(f"City: {s.city}")