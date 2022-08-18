
# 1. import list
# 2. finde division index
# 3. divide list in to chunks
# 4. join chunks in to single objects
# 5. return data

from itertools import islice

def basic_divider( data, orders_list ):
    
    orders = orders_list
    new_data = []
    order_index = []

    # 1. import and split data
    data = data.split()

    # 2. finde division index
    for x in range(len(data)):
        if data[x] in orders:
            order_index.append(x)
        else:
            pass
    
    # ----- clean devision index orphan on top of the list
    if order_index[0]==0:
        del order_index[0]
    else:
        pass

    # ----- calculate cut index (chunks sizes)
    cut_index=[order_index[0]]
    for x in range(1,len(order_index)):
        cut_index.append(order_index[x]-order_index[x-1])

    # 3. divide list in to chunks base on cut index
    it = iter(data)
    chunks = [list(islice(it, 0, i)) for i in cut_index]

    for x in range(len(chunks)):
        chunks[x] = chunks[x] = " ".join(chunks[x])
        new_data.append(chunks[x])
    
    # 5. return data
    return new_data