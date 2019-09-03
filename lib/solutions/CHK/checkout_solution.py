

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_value = 0
    basedata = {'A': [50, (3, 130)],
                'B': [30, (2, 45)],
                'C': [20, None],
                'D': [15, None]
            }
    qty_matrix = get_qty_matrix()
    for sku, qty in qty_matrix.items():
        


    return total_value

def get_qty_matrix(skus):
    qty_matrix = {}

    if isinstance(skus, str):
        skus = list(skus)
        for item in skus:
            if item not in qty_matrix:
                qty_matrix[item] = 1
            else:
                qty_matrix[item] += 1  # increase count
    else:
        print("Invalid type: {}".format(type(skus)))
        return -1

    print(qty_matrix)
    return qty_matrix
