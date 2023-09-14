"""
Ikes Lemonade
File: Ikes_Lemonade_Class.py
Version: 1
Description: Ikes Lemonade Stand Class
"""
#Cost
LEMONADE_COST = 8.99

class IkesLemonade:
      def __init__(self):
            pass
      
      #lemonadeQuantity == num_of_lemonade
      def calculate(self, lemonadeQuantity):
            # TODO: Calculate Cost of lemonades purchased
            self.lemonadeQuantity = lemonadeQuantity
            self.total_bill = self.lemonadeQuantity * LEMONADE_COST

