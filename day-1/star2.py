#!/usr/bin/python3
import math

def calculate_fuel(mass: int) -> int:
    fuel = math.floor(mass / 3) - 2

    if (fuel < 0):
        return fuel

    new_fuel = calculate_fuel(fuel)
    if (new_fuel > 0):
        fuel += new_fuel
    return fuel


with open("input.txt") as file:
    content = file.readlines()

content = [x.strip() for x in content]

total_fuel = 0;

for line in content:
    mass = int(line)
    fuel = calculate_fuel(mass)
    total_fuel += fuel

print("Total Required fuel is:", total_fuel)
