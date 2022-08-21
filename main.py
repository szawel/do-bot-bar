from lib import *
import json


def main():

    from lib import order_add
    from lib import order_del
    from lib import order_show
    from lib import order_end

    orders_list = []
    utility_list = []
    command = []
    user_order_lists = LoadOrders()
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