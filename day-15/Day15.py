# A dictionary containing drink details, ingredients, and costs.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# A dictionary to track the current resources of the coffee machine.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(drink_name):
    """
    Checks if there are enough resources to make the selected drink.
    Returns True if resources are sufficient, False otherwise.
    Prints a comprehensive message of all missing items if any.
    """
    order_ingredients = MENU[drink_name]["ingredients"]
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction(order, user_money):
    """
    Checks if the money is enough to purchase the drink and handles change/refund.
    Returns True on success, False on failure.
    """
    global resources
    coffee_cost = MENU[order]['cost']
    if coffee_cost > user_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif user_money > coffee_cost:
        change = round(user_money - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += coffee_cost
        return True
    else:  # user_money == coffee_cost
        resources["money"] += coffee_cost
        return True


def make_coffee(order):
    """
    Deducts the required ingredients from the machine's resources.
    """
    global resources
    order_ingredients = MENU[order]["ingredients"]
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order}. Enjoy!")


# --- Main Program Loop ---
coffeemachine_on = True

while coffeemachine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        coffeemachine_on = False
    elif order == "report":
        # Print a report of current resources from the 'resources' dictionary
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif order in MENU:
        # 1. Check if resources are sufficient
        if check_resources(order):
            # 2. Process coins
            payment = process_coins()
            # 3. Check if transaction is successful
            if transaction(order, payment):
                # 4. Make the coffee and deduct resources
                make_coffee(order)
    else:
        print("Invalid drink order. Please select from the menu.")
        
