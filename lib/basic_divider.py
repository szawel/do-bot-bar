
# 1. import list
# 2. finde division index
# 3. divide list in to chunks
# 4. join chunks in to single objects
# 5. return data

from itertools import islice

def BasicDivider( data ):
    
    temp_list = ["#add", '#del']

    orders = temp_list
    new_data = []
    order_index = []
    chunks = []

    # 1. import and split data
    data = data.split()

    print('imput data:      ', data)

    # 2. finde division index
    for x in range(len(data)):
        if data[x] in orders:
            order_index.append(x)
        else:
            pass
    
    # add len of data on the end of list
    order_index.append(len(data))

    for x in range(len(order_index)-1):
        chunk = list(data[order_index[x]:order_index[x+1]])
        chunks.append(chunk)

    print('chunks:          ', chunks)

    # ----- calculate cut index (chunks sizes)
    cut_index=[]
    for x in range(0,len(order_index)):
        cut_index.append(order_index[x]-order_index[x-1])

    for x in range(len(chunks)):
        chunks[x] = chunks[x] = " ".join(chunks[x])
        new_data.append(chunks[x])

    # 5. return data
    return new_data

# temp = BasicDivider('#add 1 2 3 #add 4 5 #add 6 7 8 9')
# print("----- ----- ----- ----- -----")
# print('                 ', temp)

# for x in temp:
#     print(x)