#!/usr/bin/python3

import sys

if __name__ == "__main__":
    nbr_list = []
    print("=== Player Score Analytics ===")
    for number in sys.argv[1:]:
        try:
            nbr_list.append(int(number))
        except ValueError:
            print(f"Invalid parameter: {number}")
    if len(nbr_list) == 0:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        print(f"Scores processed: {nbr_list}")
        print(f"Total players: {len(nbr_list)}")
        print(f"Total score: {sum(nbr_list)}")
        print(f"Average score: {sum(nbr_list) / len(nbr_list)}")
        print(f"High score: {max(nbr_list)}")
        print(f"Low score: {min(nbr_list)}")
        print(f"Score range: {max(nbr_list) - min(nbr_list)}")
