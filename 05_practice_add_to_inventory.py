# List to Dictionary Function For Fantasy Game Invetory

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))


def addInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.setdefault(item, 0) + 1

        # if item in inventory:  # inventory.keys()
        #    inventory[item] += 1
        # else:
        #    inventory[item] = 1


displayInventory(inv)
addInventory(inv, dragonLoot)
displayInventory(inv)
