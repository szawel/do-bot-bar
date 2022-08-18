from lib import *
import json


def main():

    # load order file
    with open('settings\orders.json') as f:
        data = json.load(f)

    # 1. load orders list
    for state in data['user_orders']:
        orders_list = state['list_orders']

    # 2. load utility orders list 
    for state in data['user_orders']:
        utility_list = state['utility_orders']

    # merge list of posibel orders
    user_order_lists = orders_list + utility_list

    order_add("some data")

    # 3. Run main while
    while True:
        print("                              ")
        user_input = input('Type new order: ')
        user_input = BasicInterpreter(user_input, user_order_lists)
        user_input = user_input.split()

        if len(user_input) != 0:
            if user_input[0] in orders_list:
                print("new order: ", user_input, end='\n')
                # user_input = locals()[user_input]
                # user_input(user_input)
            elif user_input[0] in utility_list:
                print("Utilty order: ", user_input, end='\n')
                # user_input = locals()[user_input]
                # user_input()
            else:
                print('nothing can be done with given data' , end='\n')
                print("                              ")
        else:
            print('! no data or no useful data was given !' , end='\n')
            pass


if __name__ == '__main__':
    main()
else:
    pass