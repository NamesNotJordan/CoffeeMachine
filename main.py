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
    print(f"water")


def check_resources_for_drink(drink):
    return drink['water'] <= resources['water'] & drink['milk'] <= resources['milk'] & drink['coffee'] <= resources['coffee']


while True:
    choice = input("What can I get you, Friend? (espresso/latte/cappuccino):")
    if choice == 'off':
        break
    elif choice == 'report':
        report_resources()
    elif choice == 'espresso':
        pass
    elif choice == 'latte':
        pass
    elif choice == 'cappuccino':
        pass