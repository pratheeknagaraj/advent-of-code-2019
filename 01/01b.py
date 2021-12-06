#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

def calc_fuel(n):
    val = (n // 3) - 2
    val = max(0, val)
    if val > 0:
        val += calc_fuel(val)
    else:
        return 0
    return val

# Tests

# print(calc_fuel(14))
# print(calc_fuel(1969))
# print(calc_fuel(100756))

total = 0

for l in lines:
    total += calc_fuel(int(l))

print(total)
