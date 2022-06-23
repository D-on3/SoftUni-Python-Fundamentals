def is_item_exist(groceries_list, idx):
    return True if idx in groceries_list else False


def urgent(groceries_list, item_add):
    if not is_item_exist(groceries_list, item_add):
        groceries_list.insert(0, item_add)
    return groceries_list


def unnecessary(groceries_list, item_remove):
    if is_item_exist(groceries_list, item_remove):
        groceries_list.pop(item_remove)
    return groceries_list


def correct(groceries_list, old, new):
    if is_item_exist(groceries_list, old):
        old_index = groceries_list.index(old)
        groceries_list.remove(old)
        groceries_list.insert(old_index, new)
    return groceries_list


def rearrange(groceries_list, item_rearrange):
    if is_item_exist(groceries_list, item_rearrange):
        groceries_list.remove(item_rearrange)
        groceries_list.append(item_rearrange)
    return groceries_list


groceries = input().split("!")

line = input()

while not line == "Go Shopping!":
    command = line.split()[0]
    item = line.split()[1]

    if command == "Urgent":
        groceries = urgent(groceries, item)
    elif command == "Unnecessary":
        groceries = unnecessary(groceries, item)
    elif command == "Correct":
        new_item = line.split()[2]
        groceries = correct(groceries, item, new_item)
    elif command == "Rearrange":
        groceries = rearrange(groceries, item)

    line = input()

print(', '.join(groceries))
