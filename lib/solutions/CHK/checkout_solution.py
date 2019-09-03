

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_value = 0
    basedata = {'A': [50, (3, 130)],
                'B': [30, (2, 45)],
                'C': [20, None],
                'D': [15, None]
            }
    qty_matrix = get_qty_matrix(skus)
    for sku, qty in qty_matrix.items():
        if sku in basedata:
            if isinstance(basedata[sku][1], tuple):
                # check if special offer is present
                full_bundles = qty // basedata[sku][1][0]
                left_over = qty % basedata[sku][1][0]
                sku_cost = (full_bundles * basedata[sku][1][1]) + (left_over * basedata[sku][0])
                total_value += sku_cost
            else:
                # no bundle offers are present
                sku_cost = qty * basedata[sku][0]
                total_value += sku_cost
        else:
            # sku price is not declared beforehand, hence can't compute value
            return -1

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

    # print(qty_matrix)
    return qty_matrix


# print(checkout("ABAABCA"))
# print(checkout("ACCDD"))
print(checkout(""))
