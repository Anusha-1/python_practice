class Wallet(object):
    def __init__(self,initital_amount=0):
        self.balance=initital_amount

    def add_cash(self,amount):
        self.balance +=amount

    def spend_cash(self,amount):
        if self.balance<amount:
            raise InsufficientFunds(f"Not enough amount in wallet! {self.balance}")
        self.balance -=amount

class InsufficientFunds(Exception):
    pass