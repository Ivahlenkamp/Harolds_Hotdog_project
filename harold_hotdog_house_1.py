"""
Ikes Lemonade
File: harold_hotdog_house_1.py
Version: 1
Description: POS program
"""

#Cost
LEMONADE_COST = 8.99



# TODO: Get int input from user how may lemonades sold 

num_of_lemonades= int(input("Quantity of Lemonades purchased: "))

# TODO: Calculate Cost of lemonades purchased
total_bill = num_of_lemonades * LEMONADE_COST

#TODO: Display transaction to customer
print(f"Your total cost ${total_bill:,.2f}")