from lib import *

orders_list = ['#add', '#del'] #list of list operation functions
utils_list = ['#end', '#show'] #list of utility functions

# a_list = ['kon']

# while True:
#     user_function = input('Wybierz fuinkcje: ')
#     if user_function in f_list:
#         user_input = input('podaj dane: ')
#         user_function = locals()[user_function]
#         user_function(user_input)
#     elif user_function in u_list:
#         user_function = locals()[user_function]
#         user_function()
#     else:
#         print('nie ma takiej funkcji ani operacji' , end='\n')

# from lib.core import basic

# while True:
#     user_input = input()
#     todo = basic(user_input)
#     print(todo[0], todo[1])


def main():


    while True:
        print("----- ----- ----- ----- ----- ")
        user_input = input('Wybierz fuinkcje: ')
        user_input = BasicInterpreter(user_input, orders_list)
        user_input = user_input.split()

        if user_input[0] in orders_list:
            print("new order: ", user_input)
            # user_input = locals()[user_input]
            # user_input(user_input)
        elif user_input[0] in utils_list:
            print("Utilty order: ")
            # user_input = locals()[user_input]
            # user_input()
        else:
            print('nothing that can be done was given' , end='\n')


if __name__ == '__main__':
    main()
else:
    pass