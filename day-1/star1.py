#!/usr/bin/python3
import math

with open("input.txt") as file:
    content = file.readlines()

content = [x.strip() for x in content]

total_fuel = 0

for line in content:
    mass = int(line)
    fuel = math.floor(mass / 3) - 2
    total_fuel += fuel

print("Total Required fuel is:", total_fuel)
