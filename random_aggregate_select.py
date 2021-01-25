import random   

def get_items_selected_percentages(items_selected: dict) -> dict:
    items_count = 0
    items_dict = {}
    
    for value in items_selected.values():
        items_count += value

    for key, val in items_selected.items():
        items_dict[key] = "{:.2f}%".format((val / items_count) * 100)

    return items_dict

#
def random_aggregate_item_select_type_deco(fn):
    items_amount_dict = {str: int}
    items_list = [str]

    def wrapper(iterations: int, items: items_list) -> items_amount_dict:
        return fn(iterations, items)
    
    return wrapper

@random_aggregate_item_select_type_deco
def random_aggregate_item_select(iterations, items):
    items_amount = {}

    for _ in range(iterations):
        item_index = random.randint(0, len(items) - 1)
        item_selected = items[item_index]

        if item_selected in items_amount:
            items_amount[item_selected] += 1
        else:
            items_amount[item_selected] = 1

    return items_amount


# example
items_selected_100 = random_aggregate_item_select(100, ["heads", "tails"])

print(get_items_selected_percentages(items_selected_100))