# Core function

# basic_interpreter
# stands in the first line of defense,
# against nonsense entered by the [user],
# filters and cleans [data], removes empty [orders]
# removes [data] without [orders]

# 1. split [user] [data] in to list
# 2. clean up, remove [order] without [content]
# 3. clean up, remove [order] orphan from end of list
# 4. clean up, remove [order] orphan from top of list
# 5. clean list if lenght <=2

def BasicInterpreter( data, orders ):
    
    orders_list = orders           # list of [orders]
    user_data = []                  # empty list to store [user] [date]
    io_num = 0                      # io_num = initial orphan number + index,

    # 1. split in to list of objects,
    # get lenght and
    # add empty object to the end, it will be removed in proces
    data = data.split()
    lenght = len(data)
    data.append('')

    # 2. remove orphan, [orders] without [content]
    for x in range(lenght):
        if data[x] in orders_list and data[x+1] in orders_list:
            pass
        else:
            user_data.append(data[x])

    # 3. orphan [order] clean up, remove orphan from end of list
    if user_data[-1] in orders_list:
        del user_data[-1]

    # 4. orphan [content] clean up, remove orphanfrom the top of the list
    # by using [io_num] to determin list slice cut 
    for x in range(len(user_data)):
        if user_data[x] in orders_list:
            break
        else:
            io_num=x

    # if [io_num] is equal to [0]
    # that means there is no [content] orphan to clean up
    # else its means there is orphan clean up to do, add [1] 
    if io_num == 0:
        pass
    else:
        io_num = io_num+1

    # orphan to clean up from top of the list
    user_data=user_data[io_num:]

    # clear list if ther is less then one object
    if len(user_data)<=1:
        user_data.clear()
    else:
        pass
    
    user_data = " ".join(user_data)

    return user_data