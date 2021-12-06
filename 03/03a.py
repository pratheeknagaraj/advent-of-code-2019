#!/usr/bin/python3

with open('03_input', 'r') as f:
    lines = f.readlines()

wire1 = lines[0].strip().split(',')
wire2 = lines[1].strip().split(',')

def get_points(wire):
    pos = (0,0)
    all_pts = set()
    for segment in wire:
        direction = segment[0]
        dist = int(segment[1:])
        if direction == 'R':
            pts = set([(x, pos[1]) for x in range(pos[0], pos[0] + dist + 1)])
            pos = (pos[0] + dist, pos[1])
        elif direction == 'L':
            pts = set([(x, pos[1]) for x in range(pos[0], pos[0] - dist - 1, -1)])
            pos = (pos[0] - dist, pos[1])
        elif direction == 'U':
            pts = set([(pos[0], y) for y in range(pos[1], pos[1] + dist + 1)])
            pos = (pos[0], pos[1] + dist)
        elif direction == 'D':
            pts = set([(pos[0], y) for y in range(pos[1], pos[1] - dist - 1, -1)])
            pos = (pos[0], pos[1] - dist)
        all_pts |= pts
    return all_pts

points1 = get_points(wire1)
points2 = get_points(wire2)

common = points1 & points2
min_dist = float("inf")

for pt in common:
    manhattan_dist = abs(pt[0]) + abs(pt[1])
    if manhattan_dist > 0 and manhattan_dist < min_dist:
        min_dist = manhattan_dist

print(min_dist)
