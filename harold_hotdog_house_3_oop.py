"""
Ikes Lemonade
File: harold_hotdog_house_2_functional.py
Version: 1
Description: Functional POS program
"""

#Cost
LEMONADE_COST = 8.99

class IkesLemonade:
      def __init__(self):
            pass

      def get_input(self):
            # TODO: Get int input from user how may lemonades sold 

            self.num_of_lemonades= int(input("Quantity of Lemonades purchased: "))


      def calculate(self):
            # TODO: Calculate Cost of lemonades purchased
            self.total_bill = self.num_of_lemonades * LEMONADE_COST


      def display(self):
            #TODO: Display transaction to customer
            print(f"Your total cost ${self.total_bill:,.2f}")

Ikes_Lemonade= IkesLemonade()
Ikes_Lemonade.get_input()
Ikes_Lemonade.calculate()
Ikes_Lemonade.display()