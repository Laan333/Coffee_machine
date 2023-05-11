from data.menu_coffee import *

def check_resources(user_answer):
    ingr=MENU[user_answer]["ingredients"]
    coffe_resources_keys= list(ingr.keys())
    coffee_machine_resouces_keys = list(resources.keys())
    for j in range(len(coffe_resources_keys)):
        if ingr[coffe_resources_keys[j]] <= resources[coffee_machine_resouces_keys[j]]:
            pass
        else:
            print(f"Not enough {coffee_machine_resouces_keys[j]}")
            return False
        return True
def place_money():
    user_money_quarters = int(input("Place your quarters, how many?: "))
    user_money_dimes = int(input("Place your dimes, how many?: "))
    user_money_nickles = int(input("Place your nickles, how many?: "))
    user_money_pennies = int(input("Place your pennies, how many?: "))
    calculate = user_money_quarters * 0.25 + user_money_dimes * 0.10 + user_money_nickles * 0.05\
                + user_money_pennies * 0.01
    return calculate
def transaction(user_answer):
    global money_data
    money_coffee = MENU[user_answer]["cost"]
    money_user = place_money()
    if money_user == money_coffee:
        money_data += money_user
        return True
    elif money_user > money_coffee:
        cashback = money_user - money_coffee
        money_data += money_coffee
        cashback = round(cashback, 2)
        print(f"Take your cash :) ${cashback}")
        return True
    else:
        print(f"Not Enough Money, take your money back {money_user}")
        return False

def make_coffee(user_answer):
    coffee_ingr = MENU[user_answer]["ingredients"]
    coffee_keys = list(coffee_ingr.keys())
    for i in range(len(coffee_keys)):
        resources[coffee_keys[i]] = resources[coffee_keys[i]] - coffee_ingr[coffee_keys[i]]
    return True

def operations(user_answer):
    if check_resources(user_answer):
        if transaction(user_answer):
            if make_coffee(user_answer):
                print("Take your coffee")
def start():
    while True:
        user_answer = input("What would you like?(espresso/latte/cappuccino): ")
        if user_answer == "espresso":
            operations(user_answer)
        elif user_answer == "latte":
            operations(user_answer)
        elif user_answer == "cappuccino":
            operations(user_answer)
        elif user_answer == "off":
            exit()
        elif user_answer == "report":
            print(f"${money_data}")
            for i in resources:
                print(f"{i}:{resources[i]}")

if __name__ == '__main__':
    start()