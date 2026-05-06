#!/usr/bin/python3


import random
import typing

names = ["Alice", "Bob", "Charlie", "Dylan"]
actions = ["move", "eat", "grab", "release"]
event_lst_size = 10

def gen_event() -> typing.Generator[tuple, None, None]:
	yield (random.choice(names), random.choice(actions))


def consume_event(e_lst: list[tuple] = []) -> typing.Generator[tuple, None, None]:
	while len(event_list) > 0:
		yield e_lst.pop(random.randint(0,len(e_lst) - 1))


if __name__ == "__main__":
	print("=== Game Data Stream Processor ===")
	for id in range(0,1000):
		event = next(gen_event())
		print(f"Event {id}: Player {event[0]} did action {event[1]}.")
	event_list = []
	for _ in range(0, event_lst_size):
		event_list.append(next(gen_event()))
	print(f"Built list of {event_lst_size} events: {event_list}")
	for event in consume_event(event_list):
		print(f"Got event from list: {event}")
		print(f"Remains in list: {event_list}")
