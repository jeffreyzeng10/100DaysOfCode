from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


if __name__ == '__main__':
    while True:
        choice = input("What would you like next? (expresso/latte/cappuccino/): ")
        if choice == 'off':
            break
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        menu_item = menu.find_drink(choice)
        
        # check for sufficient resources
        if coffee_maker.is_resource_sufficient(menu_item):
            money_machine.make_payment(menu_item.cost)
            coffee_maker.make_coffee(menu_item)
        else:
            break
        
