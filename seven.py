import time

from config import input_path
import os

start_time = time.time()

with open(os.path.join(input_path, 'input7.txt'), 'r') as file:
    lines = [line.strip().split() for line in file.readlines()]


def determine_hand(hand):
    cards = dict(zip('2 3 4 5 6 7 8 9 T J Q K A'.split(), range(14)))
    hand_rank = [cards[a] for a in hand]

    num_cards = sorted([a for a in [[x for x in hand].count(a) for a in cards] if a > 0])

    if num_cards == [5]:
        hand_rank.insert(0, 7)
        return hand_rank
    elif num_cards == [1, 4]:
        hand_rank.insert(0, 6)
        return hand_rank
    elif num_cards == [2, 3]:
        hand_rank.insert(0, 5)
        return hand_rank
    elif num_cards == [1, 1, 3]:
        hand_rank.insert(0, 4)
        return hand_rank
    elif num_cards == [1, 2, 2]:
        hand_rank.insert(0, 3)
        return hand_rank
    elif num_cards == [1, 1, 1, 2]:
        hand_rank.insert(0, 2)
        return hand_rank
    else:
        hand_rank.insert(0, 1)
        return hand_rank


def determine_hand_2(hand):
    cards = dict(zip('J 2 3 4 5 6 7 8 9 T Q K A'.split(), range(14)))
    hand_rank = [cards[a] for a in hand]

    num_cards = sorted([a for ind, a in enumerate([[x for x in hand].count(a) for a in cards]) if a > 0 and ind > 0])

    if len(num_cards) > 0:
        num_cards[-1] += 5 - sum(num_cards)
    else:
        num_cards = [5]

    if num_cards == [5]:
        hand_rank.insert(0, 7)
        return hand_rank
    elif num_cards == [1, 4]:
        hand_rank.insert(0, 6)
        return hand_rank
    elif num_cards == [2, 3]:
        hand_rank.insert(0, 5)
        return hand_rank
    elif num_cards == [1, 1, 3]:
        hand_rank.insert(0, 4)
        return hand_rank
    elif num_cards == [1, 2, 2]:
        hand_rank.insert(0, 3)
        return hand_rank
    elif num_cards == [1, 1, 1, 2]:
        hand_rank.insert(0, 2)
        return hand_rank
    else:
        hand_rank.insert(0, 1)
        return hand_rank


def task1():
    for ind, hand in enumerate(lines):
        rating = determine_hand(hand[0])
        lines[ind].append(rating)
    lines.sort(key=lambda x: x[2])
    answer = sum([ind * int(x[1]) for ind, x in enumerate(lines, 1)])
    print(f"The answer for part one is {answer}\n")


def task2():
    for ind, hand in enumerate(lines):
        rating = determine_hand_2(hand[0])
        lines[ind].append(rating)
    lines.sort(key=lambda x: x[2])
    answer = sum([ind * int(x[1]) for ind, x in enumerate(lines, 1)])
    print(f"The answer for part two is {answer}\n")


if __name__ == "__main__":
    task1()
    task2()
    print(f"Script runs in {time.time() - start_time} seconds")
