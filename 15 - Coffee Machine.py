MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}



def start():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    
    #turn machine off
    if order == 'off':
        return()
    
    #print report
    elif order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']}")
        return start()
    else:
        #check for resource shortage
        shortage = check_resources(order)
        if shortage != None:
            print(f"Sorry there is not enough {shortage}.")
            return
        
        #request payment
        print('Please insert coins')
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
        
        #calculate if customer can afford drink
        if total < MENU[order]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        
        #deduct resources from making drink
        resources['water'] -= MENU[order]['ingredients']['water']
        resources['coffee'] -= MENU[order]['ingredients']['coffee']
        resources['milk'] -= MENU[order]['ingredients']['milk']     
        #add sale to money   
        resources['money'] += MENU[order]['cost']

        #return change
        if total > MENU[order]['cost']:
            change = total - MENU[order]['cost']
            change = round(change,2)
            print(f"Here is ${change} in change. ")
            
        print(f"Here is your {order}. Enjoy!")
        return start()

#checks if machine has enough resources to make drink
def check_resources(order):
    if MENU[order]['ingredients']['water'] > resources['water']:
        return 'water'
    
    elif MENU[order]['ingredients']['coffee'] > resources['coffee']:
        return 'coffee'

    elif MENU[order]['ingredients']['milk'] > resources['milk']:
        return 'milk'
    else:
        return


start()
