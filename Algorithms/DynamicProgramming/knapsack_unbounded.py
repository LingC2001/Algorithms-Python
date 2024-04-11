
def knapsack_unbounded_TD(values, weights, capacity):
    if len(values) == 0 or capacity <= 0:
        return 0, []
    max_values = [None] * (capacity+1)
    best_items = [None] * (capacity+1)
    min_weight = min(weights)
    max_values[capacity] = knapsack_memo(values, weights, capacity, max_values, best_items, min_weight)

    items_taken = get_items(weights, best_items, min_weight, capacity)

    return max_values[capacity], items_taken
    

def knapsack_memo(values, weights, capacity, max_values, best_items, min_weight):

    if capacity < min_weight: # base case
        return 0
    
    elif max_values[capacity] is None: # calculate is not in memoisation table already
        max_values[capacity] = -1
        for item in range(len(values)):
            if weights[item] <= capacity:
                value_with_item = values[item] + knapsack_memo(values, weights, capacity-weights[item], max_values, best_items, min_weight)
                if value_with_item > max_values[capacity]:
                    max_values[capacity] = value_with_item
                    best_items[capacity] = item

    # get answer from memoisation table
    return max_values[capacity]

def get_items(weights, best_items, min_weight, capacity):
    if best_items[capacity] is None:
        return []
    
    items = []
    while capacity >= min_weight:
        items.append(best_items[capacity])
        capacity -= weights[best_items[capacity]]
    return items


def knapsack_unbounded_BU(values, weights, capacity):
    if len(values) == 0 or capacity <= 0:
        return 0, []
    max_values = [0] * (capacity+1)
    best_items = [None] * (capacity+1)
    min_weight = min(weights)

    for c in range(min_weight, capacity+1):
        for item in range(len(values)):
            if weights[item] <= c:
                new_value = values[item] + max_values[c-weights[item]]
                if new_value > max_values[c]:
                    max_values[c] = new_value
                    best_items[c] = item
    
    items_taken = get_items(weights, best_items, min_weight, capacity)

    return max_values[capacity], items_taken            

    