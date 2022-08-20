from lib import *
import json


def main():

    from lib import order_add
    from lib import order_del

    orders_list = []
    utility_list = []
    command = []
    
    # load order file nad all lists
    with open('settings\orders.json') as f:
        data = json.load(f)

    for state in data['user_orders']:
        orders_list = state['orders']

    user_order_lists = orders_list

    # main loop
    while True:

        # take input
        user_input = input('Type new order: ')


        # pass input through Interpreter and Divider
        user_input = BasicInterpreter(user_input, user_order_lists)
        user_input = BasicDivider(user_input, user_order_lists)

        # run if user_input exist / pass classes above
        if user_input!=[]:

            for x in user_input:
                data = x.split()
                order = " ".join(data[:1])
                content = " ".join(data[1:])

                if order in user_order_lists:
                    order = order.replace("#", "order_")

                    run =locals()[order]
                    run(content)
                else:
                    pass


if __name__ == '__main__':
    main()
# else:
#     pass