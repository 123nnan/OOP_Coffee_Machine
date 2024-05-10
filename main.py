from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
option = menu.get_items()

while is_on:
    user_choice = input(f"What coffee do you like? {option.strip("/")}: ")

    if user_choice == 'off':
        is_on = False

    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
