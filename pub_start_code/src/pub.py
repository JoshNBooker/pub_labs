class Pub:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def change_till_by_amount(self, amount):
        self.till += amount
        return self.till

    
    def sell_drink(self, drink):
        drink_price = drink.price
        self.change_till_by_amount(drink_price)
        return self.till