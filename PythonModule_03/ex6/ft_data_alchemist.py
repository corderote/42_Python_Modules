#!/usr/bin/python3


import random

names = ['Alice', 'bob', 'Charlie',
         'dylan', 'Emma', 'Gregory',
         'john', 'kevin', 'Liam']


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    all_capitalize_lst = [name.capitalize() for name in names]
    print(f"New list with all names capitalized: {all_capitalize_lst}")
    only_capitalize = [name for name in names if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_capitalize}")
    score_dict = {name: random.randint(0, 1000) for name in all_capitalize_lst}
    print(f"Score dict: {score_dict}")
    average = round(sum(list(score_dict.values()))/len(score_dict), 2)
    print(f"Score average is {average}")
    higs_scores = {name: score
                   for name, score in score_dict.items()
                   if score > average}
    print(f"High scores: {higs_scores}")
