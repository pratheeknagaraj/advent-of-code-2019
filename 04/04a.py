#!/usr/bin/python3

with open('04_input', 'r') as f:
    lines = f.readlines()

start, end = [int(i) for i in lines[0].strip().split('-')]

def valid(n):
    n_str = str(n)

    if sorted(n_str) != list(n_str):
        return False

    if n_str[0] == n_str[1] or \
        n_str[1] == n_str[2] or \
        n_str[2] == n_str[3] or \
        n_str[3] == n_str[4] or \
        n_str[4] == n_str[5]:
        return True

    return False

count = 0
for i in range(start, end + 1):
    count += valid(i)

print(count)
