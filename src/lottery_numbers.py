# Write your solution here

from random import *


def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        # for i in range(amount):
        r1 = randint(lower, upper)
        if r1 not in numbers:
            numbers.append(r1)
    return sorted(numbers)
