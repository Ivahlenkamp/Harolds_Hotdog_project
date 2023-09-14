"""
Ikes Lemonade
File: harold_hotdog_house_2_functional.py
Version: 1
Description: Functional POS program
"""

#Cost
LEMONADE_COST = 8.99

def main():
      number_of_lemonades = get_input()
      total_sale = calculate(number_of_lemonades)
      display(total_sale)

def get_input():
      # TODO: Get int input from user how may lemonades sold 

      num_of_lemonades= int(input("Quantity of Lemonades purchased: "))
      return num_of_lemonades

def calculate(num_of_lemonades):
      # TODO: Calculate Cost of lemonades purchased
      total_bill = num_of_lemonades * LEMONADE_COST
      return total_bill

def display(total_bill):
      #TODO: Display transaction to customer
      print(f"Your total cost ${total_bill:,.2f}")

if __name__ == '__main__':
      main()