MENU={
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
    "ingredients": {
        "water": 200,
        "coffee": 140,
        "milk": 150,
    },
    "cost": 2.5,
},
    "capuccino":{
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
         },
        "cost": 3.0,
},
}
resources = {
"water": 300,
"milk": 200,
"coffee": 100,


}
selection=""
money_current=0
def report():
    print (f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money_current}")


def check_ingredients(selection):
    if selection!="espresso" and int(MENU[selection]["ingredients"]["milk"])>int(resources["milk"]):
        print("Sorry there is not enough milk")
        return 1
    elif int(MENU[selection]["ingredients"]["water"])>int(resources["water"]):
        print("Sorry there is not enough water")
        return 2 
    elif int (MENU[selection]["ingredients"]["coffee"])>int(resources["coffee"]):
        print("Sorry there is not enough coffee")
        return 3 
    else: 
        return 0
def check_money(money_input,selection):
    global money_current
    if float(money_input)==float(MENU[selection]["cost"]):
        return 0
    elif float(money_input)>float(MENU[selection]["cost"]):
        return 1
    else: 
        return 2
def change(selection, money_input):
    global money_current
    change2=0
    change2=money_input-float(MENU[selection]["cost"])
    print(f"Here's your change: ${change2} ")

def make_coffee(selection):
    global resources
    global money_current
    resources["water"]-=MENU[selection]["ingredients"]["water"]
    resources["coffee"]-=MENU[selection]["ingredients"]["coffee"]
    money_current+= MENU[selection]["cost"]
    if selection!="espresso":
        resources["milk"]-=MENU[selection]["ingredients"]["milk"]
go_on="Y"




while (go_on=="Y"):
    selection=input("What would you like to order?(espresso, latte, capuccino) ")
    if selection=="report":
        report()
    else:
        if (check_ingredients(selection)==0):
            pennies=float(input("How many pennies would you like to put in? "))
            nickles=float(input("How many nickles would you like to put in? "))
            dimes=float(input("How many dimes would you like to put in? "))
            quarters=float(input("How many quarters would you like to put in? "))
            money_input= 0.01*pennies+0.05*nickles+0.1*dimes+0.25*quarters
            if check_money(money_input, selection)==1:
                change(selection, money_input)
                make_coffee(selection)
            elif check_money(money_input,selection)==0: 
                make_coffee(selection)
            else: 
                print("Sorry there is not enough money")
    go_on=input("Would you like to order again? (Y/N): ").upper()