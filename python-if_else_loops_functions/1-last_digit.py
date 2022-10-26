#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdg = abs(number) % 10
if number < 0:
        lastdg *= (-1)
if lastdg > 5:
    print(f"Last digit of {number} is {lastdg} and is greater than 5")
elif lastdg == 0:
    print(f"Last digit of {number} is {lastdg} and is 0")
else:
    print(f"Last digit of {number} is {lastdg} and is less than 6 and not 0")
