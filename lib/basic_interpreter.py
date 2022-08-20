# BasicInterpreter - first line of "defense" 
# Filters and cleans data
# Removes empty [orders]
# Removes [data] without [orders]
# Removes [orders] duplicate - empty [orders]

# 1. Check if input data contains any data
# 2. Split data
# 3. clean up orphan, remove [order] without [content]
# 4. clean up orphan, remove [order] orphan from end of list
# 5. clean up orphan, remove [order] orphan from top of list
# 6. clean list if lenght <=2

def BasicInterpreter( data, orders ):
    
    orders_list = orders
    user_data = []
    io_num = 0

    # 1. Check if input data contains any data
    if len(data)==0:
        out_data = []
    else:

        # 2. split in to list of objects,
        data = data.split()
        # calculate lenght before adding empty entry
        lenght = len(data)
        
        # add empty entry on the end
        data.append('')

        # 3. clean up orphan, [order] without [content]
        for x in range(lenght):
            if data[x] in orders_list and data[x+1] in orders_list:
                pass
            else:
                user_data.append(data[x])

        # # 4. clean up orphan, orphan [order] from end of list
        if user_data[-1] in orders_list:
            del user_data[-1]

        # 5. clean up orphan, remove [order] orphan from top of list
        # by using [io_num] to determin list slice cut 
        for x in range(len(user_data)):
            if user_data[x] in orders_list:
                break
            else:
                io_num=x

        # if [io_num] is equal to [0]
        # that means there is no [content] orphan to clean up
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
        
        out_data = " ".join(user_data)

    return out_data