#!/usr/bin/python3

import math


def get_player_pos() -> tuple[float, float, float]:
    valid = False
    while not valid:
        valid = True
        pos_str = input("Enter new coordinates as floats in format 'x,y,z': ")
        pos_lst = str.split(pos_str, ',')
        if len(pos_lst) != 3:
            print("Invalid syntax")
            valid = False
        else:
            for idx in range(0, len(pos_lst), 1):
                try:
                    float((pos_lst[idx]))
                except ValueError as error_msg:
                    print(f"Error on parameter '{pos_lst[idx]}': {error_msg}")
                    valid = False
    return (float(pos_lst[0]), float(pos_lst[1]), float(pos_lst[2]))


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got the first tuple: {p1}")
    print(f"It includes X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    distance = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(distance, 4)}")
    print()
    p2 = get_player_pos()
    distance = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2
    distance = math.sqrt(distance)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
