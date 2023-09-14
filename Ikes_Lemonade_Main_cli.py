"""
Ikes Lemonade
File: Ikes_Lemonade_Main_Cli.py
Version: 1
Description: Main Client to Access Classes
"""
import Ikes_Lemonade_Class as Get_Lemonade


def get_input():
    # TODO: Get int input from user how may lemonades sold
    num_of_lemonades = int(input("Quantity of Lemonades purchased: "))
    return num_of_lemonades


def display():
    # TODO: Display transaction to customer
    num_of_lemonades = Ikes_Lemonade.lemonadeQuantity
    total_sale = Ikes_Lemonade.total_bill
    print(f"Number of Drinks: {num_of_lemonades}")
    print(f"Your total cost ${total_sale:,.2f}")


#
Ikes_Lemonade = Get_Lemonade.IkesLemonade()
num_of_lemonades = get_input()

Ikes_Lemonade.calculate(num_of_lemonades)
display()
