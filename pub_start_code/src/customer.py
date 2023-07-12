class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def reduce_wallet(self, amount):
        self.wallet -= amount
        return self.wallet
    
    def buy_drink(self, drink):
        self.reduce_wallet(drink.price)
        
