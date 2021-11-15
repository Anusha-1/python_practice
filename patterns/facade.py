"""
Facade pattern example 
to order the pizza: swiggyapp may be
"""

#subsystem1-module1 --order.py
class Ordering:
    def __init__(self):
        print("Ordering module created")

    def order(self):
        print("Ordering food.........")

#subsystem 2-module 2 prepare.py
class Preparing:
    def __init__(self):
        print("prepare module created")

    def prepare(self):
        print("Preparing the food.........")

#subsystem 3-module 3 -deliver.py
class Delivering:
    def __init__(self):
        print("Delivery module created")

    def deliver(self):
        print("Delivering the food.........")

    def cancel(self):
        print("sorry ... order can not be cancelled............")


#facade.py
class Operator:
    """Facade"""
    def __init__(self):
        self.ordering =Ordering()
        self.preparing=Preparing()
        self.delivering =Delivering()

    def placeOrder(self):
        self.ordering.order()
        self.preparing.prepare()
        self.delivering.deliver()

#client
if __name__=='__main__':
    op=Operator()
    op.placeOrder()
    print('Enjoy the pizzaaaaa.....')