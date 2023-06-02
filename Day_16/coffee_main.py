from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# order = menu.find_drink("latte")



is_ordering = True
while is_ordering:

    print("""
    
    
    """)

    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "off":
        is_ordering = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_maker.is_resource_sufficient(menu.find_drink(order)):
        if money_machine.make_payment(menu.find_drink(order).cost):
            coffee_maker.make_coffee(order)


    print("""
    
    
    """)