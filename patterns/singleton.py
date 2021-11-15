"""
Singleton:
"""
class BankSingleton(object):
    __instance__=None

    def __init__(self):
        if BankSingleton.__instance__ is None:
           BankSingleton.__instance__=self
        else:
            raise Exception('Instance is already created and running... sorry') 

    @staticmethod  #static methods dont need the class instantiation. they can be accessed through classname.method()      
    def get_instance():
        if not BankSingleton.__instance__:
            BankSingleton()
        return BankSingleton.__instance__

b1=BankSingleton()
print(b1)
#b2=BankSingleton()
bank1=BankSingleton.get_instance()
print("first instance",bank1)
bank2=BankSingleton.get_instance()
print("second time create instance",bank2)