from lib import *
import json

def main():

    with open('settings\orders.json') as f:
        data = json.load(f)

    # load orders list
    for state in data['user_orders']:
        orders_list = state['list_orders']

    # load utility list 
    for state in data['user_orders']:
        utility_list = state['utility_orders']

    user_order_lists = orders_list + utility_list

    for i in data['user_orders']:
        print(i['list_orders'])

    while True:
        print("----- ----- ----- ----- ----- ")
        user_input = input('Wybierz fuinkcje: ')
        user_input = BasicInterpreter(user_input, user_order_lists)
        user_input = user_input.split()

        if user_input[0] in orders_list:
            print("new order: ", user_input)
            # user_input = locals()[user_input]
            # user_input(user_input)
        elif user_input[0] in utility_list:
            print("Utilty order: ", user_input)
            # user_input = locals()[user_input]
            # user_input()
        else:
            print('nothing can be done with given data' , end='\n')


if __name__ == '__main__':
    main()
else:
    pass