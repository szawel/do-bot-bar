# f_list = ['f_add', 'f_del'] #list of list operation functions
# u_list = ['f_end', 'f_show'] #list of utility functions
# a_list = ['kon']

# def f_add(data):
#     a_list.append(data)
#     print('new entrie [ ' + data + ' ]  has been added to the list !')
#     print(' ')

# def f_del(data):
#     a_list.remove(data)
#     print('entrie [ ' + data + ' ] has been removed from the list')

# def f_show():
#     print(' ')
#     print(a_list)
#     print(' ')

# def f_end():
#     print('Program zakączył prace')
#     exit()
    
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