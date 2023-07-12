import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Paul", 100)
        self.drink1 = Drink("Tennants", 4)
        self.drink2 = Drink("Guiness", 5)
        self.drink3 = Drink("Whiskey", 3.50)
        self.pub = Pub("The Devil's Backbone", 1500, [
        self.drink1, self.drink2, self.drink3])

        
    def test_change_till_by_amount (self):
        result = self.pub.change_till_by_amount(self.drink1.price)
        self.assertEqual(1504, result)

    
    def test_sell_drink(self):
        return_till = self.pub.sell_drink(self.drink1)
        self.assertEqual = (323, return_till)

