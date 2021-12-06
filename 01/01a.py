#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

def calc_fuel(n):
    return (n // 3) - 2

total = 0

for l in lines:
    total += calc_fuel(int(l))

print(total)
