from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

# --- Main Program Loop ---
coffeemachine_on = True

while coffeemachine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        coffeemachine_on = False
    elif order == "report":
        # Print a report of current resources from the 'resources' dictionary
        coffe_maker.report()
        money_machine.report()

    else:
        # 1. Check if resources are sufficient
        coffee_order = menu.find_drink(order)
        resource_sufficient = coffe_maker.is_resource_sufficient(coffee_order)

        # 2. Process coins
        customer_payment = money_machine.make_payment(coffee_order.cost)

        # 3. Check if transaction is successful
        if resource_sufficient and customer_payment:
            coffe_maker.make_coffee(coffee_order)
