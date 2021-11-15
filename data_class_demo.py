#entity ,model,Object data model,DTO
from dataclasses import dataclass

@dataclass
class Car:
    color:str
    mileage:float
    automatic:bool

car1=Car("red",23.003,True)
print(car1)
print(car1.color)