# BasicDivider - divide orders
# if input data is empty pass empty list
# if input data conteins one order pass one order
# if input data conteins meny (n) orders, divide orders in to (n) object list 

# 1. Check if input data contains any data
# 2. Split data
# 3. Finde division index by compering data_list to order_list
# 4. Divide data in to chunks
# 5. Join chunks in to single objects
# 6. return data (list of orders)

def BasicDivider( data, orders_list ):


    orders = orders_list

    order_index = []
    chunks = []
    out_data = []

    # 1. Check if user input contains any data

    if len(data)==0:
        out_data = []
    else:

        # 2. Split data
        data = data.split()

        # 3. Finde division index
        for x in range(len(data)):
            if data[x] in orders:
                order_index.append(x)
            else:
                pass
        
        # add lenght of data on the end of order_index
        order_index.append(len(data))
        
        # 4. Divide data in to chunks
        for x in range(len(order_index)-1):
            chunk = list(data[order_index[x]:order_index[x+1]])
            chunks.append(chunk)

        # 5. Join chunks in to single objects
        for x in range(len(chunks)):
            chunks[x] = chunks[x] = " ".join(chunks[x])
            out_data.append(chunks[x])


    return out_data