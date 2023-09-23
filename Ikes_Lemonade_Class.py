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
            self.menu_items = ["Original Lemonade", "Blueberry Lemonade", "Strawberry Lemonade"]
            self.menu_prices = [6.00, 7.50, 7.50]
            # initialize a cart
            self.cart =[]
      
      def get_menu_items(self) -> list:
            return self.menu_items
      
      def get_menu_prices(self) -> list:
            return self.menu_prices
      
      def display_menu(self) -> str:
            """Display menu items and prices"""
            display = ""
            for x in range(len(self.menu_items)):
                  display += f"{self.menu_items[x]} {self.menu_prices[x]}\n"
            return display
      
      #lemonadeQuantity == num_of_lemonade
      def calculate(self, lemonadeQuantity):
            # TODO: Calculate Cost of lemonades purchased
            self.lemonadeQuantity = lemonadeQuantity
            self.total_bill = self.lemonadeQuantity * LEMONADE_COST

