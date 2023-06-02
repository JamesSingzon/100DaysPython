#Print a report.
##How much water/milk/coffee it has left.
##Check resources are sufficient against drink we are trying to make.

#Process coins.
##Check transaction successful.

#Make coffee.
##Deduct resources.

def check_resources(order):
    sufficient_resources = True
    for i in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            sufficient_resources = False
    return sufficient_resources

def process_coins(order):
    cost = MENU[order]['cost']
    while cost != 0:
        print(f"Your drink will cost you ${cost:.2f}.")
        quarters = float(input("Insert # of quarters: "))
        dimes = float(input("Insert # of dimes: "))
        nickels = float(input("Insert # of nickels: "))
        pennies = float(input("Insert # of pennies: "))
        amount_paid = float(quarters)*.25 + float(dimes)*.10 + float(nickels)*.05 + float(pennies)*.01
        if cost > amount_paid:
            print("Sorry that's not enough money. Money refunded.")
        elif cost == amount_paid:
            resources["money"] = resources["money"] + amount_paid
            cost = cost - amount_paid
        else:
            change = amount_paid - cost
            print(f"Here is ${change:.2f} in change.")
            amount_paid = amount_paid - change
            resources["money"] = resources["money"] + amount_paid
            cost = cost - amount_paid

def make_coffee(order):
    for i in MENU[order]["ingredients"]:
        resources[i] = resources[i] - MENU[order]["ingredients"][i]
    print(f"Here is your {order}. Enjoy!")

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
    "money": 0,
}

prompt = True

while prompt:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        prompt = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    #check if there are enough resources to make that drink
    elif check_resources(order):
        #Proccess coins
        process_coins(order)
        #Make coffee
        make_coffee(order)