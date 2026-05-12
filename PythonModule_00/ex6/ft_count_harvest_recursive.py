def recursive_days(days: int = -1) -> None:
    if (days > 1):
        recursive_days(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive_days(days)
    print("Harvest time!")
