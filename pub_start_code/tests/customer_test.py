import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Tennants", 4)
        self.customer1 = Customer("Johnny", 80)
    
    def test_customer_has_name(self):
        self.assertEqual("Johnny", self.customer1.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(80, self.customer1.wallet)
                        
    def test_reduce_wallet(self):
        result = self.customer1.reduce_wallet(8)
        self.assertEqual(72, result)
    
    def test_buy_drink(self):
        result = self.customer1.buy_drink(self.drink1)
        self.assertEqual(4, result)