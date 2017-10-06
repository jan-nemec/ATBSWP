# Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        # print(f'{v} {k}')
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))


displayInventory(stuff)
