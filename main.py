MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
}


def check_resources(choice):
    
    
    if resources['water'] < int(MENU[choice]['ingredients']['water']):
        return ("Not sufficient water")
    elif resources['coffee']< int(MENU[choice]['ingredients']['coffee']):
        return ("Not sufficient coffee")
    elif resources['milk']< int(MENU[choice]['ingredients']['milk']):
        return ("Not sufficient milk")
    else:
        return True
    
def refund_res_update(choice):
    resources['water']=resources['water']- int(MENU[choice]['ingredients']['water'])
    resources['coffee']=resources['coffee']-int(MENU[choice]['ingredients']['coffee'])
    resources['milk']=resources['milk']-int(MENU[choice]['ingredients']['milk'])


totalmoney=0
def check_money(choice,quarter,dime,nickle,penny):
    global totalmoney
    money = quarter*0.25+ dime*0.10+ nickle*0.05+ penny*0.01
    totalmoney+=money
    if money< MENU[choice]['cost']:
        return ("Sorry that's not enough money. Money refunded.")
        
    else:
        change=round((money-MENU[choice]['cost']),2)
        if change>0:
            print (f"Here is ${change} dollars in change.")
        return True
         
 
    
    
def report():
    global totalmoney
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${totalmoney}")

machine_on=True

def coffeemachine():
    choice= input("What would you like? (espresso/latte/cappuccino)")
    if choice =="report":
        report()
    elif choice=="off":
        machine_on=False
        return
    else:
        print( f"The cost of {choice} is ${MENU[choice]['cost']}")
        a= check_resources(choice)
        # print (a)
        if a ==True:

            print("Please insert coins.")

            quarter = int(input("how many quarters?: "))
            dime = int(input("how many dimes?: "))
            nickle = int(input("how many nickles?: "))
            penny = int(input("how many pennies?: "))
            b=check_money(choice,quarter,dime,nickle,penny)
            
            if b==True:
                print(f"Here is your {choice}. Enjoy!")
                refund_res_update(choice)
            else:
                print(b)

while machine_on==True:
    coffeemachine()







