user_function = [] # empty list to store user function
user_data = [] # empty list to store user date
special_chars = set('#') # list of special characters
todel = 0

f_list = ['#add', '#del']


# take multiply inputs from user
user_input = list(map(str, input("Enter multiple values string: ").split()))

# check inputs objects for special character
# add function to "user_function" list 
# and data to "user_data" list 
lenght = len(user_input)

for i in range(lenght):
    if any((c in special_chars) for c in user_input[i]):
        todel = i
        user_function.append(user_input[i])
    else:
        user_data.append(user_input[i])

# remove objects from list the comse befour function object
user_data=user_data[todel:]
# join multiply object string in to one object
user_data = " ".join(user_data)

if user_function[0] in f_list:
    print('jest taka funkcja')
else:
    print('nie ma takiej funkcji')

# print('user_function ;', user_function)
# print('user_data ;', user_data)
