#!/usr/bin/python3


import sys


class InventoryError(Exception):
    def __init__(self, msg: str = "Unknown inventory error.") -> None:
        print(msg)


def init_inventory(items: list[str] = []) -> dict[str, int]:
    inventory = {}
    for item in items:
        try:
            aux = str.split(item, ':')
            if len(aux) != 2:
                raise InventoryError(f"Error - invalid parameter '{item}'")
            if aux[0] in inventory:
                raise InventoryError(f"Redundant item '{aux[0]}' - discarding")
            item_name = aux[0]
            item_qty = int(aux[1])
            if item_qty < 0:
                raise InventoryError(f"Invalid quantity value for '{aux[0]}': "
                                     f"'{aux[1]}' - discarding")
            inventory[item_name] = item_qty
        except ValueError:
            print(f"Quantity error for '{aux[0]}':"
                  f"invalid literal for int() with base 10: '{aux[1]}'")
        except InventoryError:
            pass
    return inventory


def add_item(inventory: dict[str, int], new_item: dict[str, int]) -> None:
    if new_item != {}:
        try:
            item = list(new_item.keys())[0]
            qty = int(list(new_item.values())[0])
            if item in inventory:
                qty += inventory[item]
            if qty < 0:
                qty = 0
            inventory[item] = qty
        except ValueError:
            print(f"Quantity error for '{item}':"
                  f"invalid literal for int() with base 10: '{qty}'")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")
        inventory = init_inventory(sys.argv[1:])
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        total = sum(list(inventory.values()))
        print(f"Total quantity of the {len(inventory)} items: {total}")
        if len(inventory) > 0:
            max_qty = max(list(inventory.values()))
            min_qty = min(list(inventory.values()))
            max_item = ""
            min_item = ""
            for item, qty in inventory.items():
                if qty == max_qty:
                    max_item = item
                if qty == min_qty:
                    min_item = item
                percentage = round(100*(float(qty)/float(total)), 1)
                print(f"Item {item} represents {percentage}%")
            print(f"Item most abundant: {max_item} with quantity {max_qty}")
            print(f"Item least abundant: {min_item} with quantity {min_qty}")
        add_item(inventory, {"magic_item": 10})
        print(f"Updated inventory: {inventory}")
        print("=== Inventory Analysis Complete ===")
    pass
