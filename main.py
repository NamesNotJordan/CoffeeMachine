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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def report_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources_for_drink(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            return False
    return True


def use_ingredients(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


while True:
    choice = input("What can I get you, Friend? (espresso/latte/cappuccino):")
    if choice == 'off':
        break
    elif choice == 'report':
        report_resources()
    else:
        drink = MENU[choice]
        print(f"okay, one {choice}!")
        if not check_resources_for_drink(drink['ingredients']):
            print(f"Sorry! Looks like we don't have enough ingredients for a {choice}")
            break
        # enough resources
        else:
            print(f"Alright! That'll be ${drink['cost']},please")
