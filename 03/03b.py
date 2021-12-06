#!/usr/bin/python3

with open('03_input', 'r') as f:
    lines = f.readlines()

wire1 = lines[0].strip().split(',')
wire2 = lines[1].strip().split(',')

def get_points(wire):
    pos = (0,0)
    all_pts = set()
    steps = 0
    step_count = dict()
    for segment in wire:
        direction = segment[0]
        dist = int(segment[1:])
        if direction == 'R':
            pts = [(x, pos[1]) for x in range(pos[0] + 1, pos[0] + dist + 1)]
            pos = (pos[0] + dist, pos[1])
        elif direction == 'L':
            pts = [(x, pos[1]) for x in range(pos[0] - 1, pos[0] - dist - 1, -1)]
            pos = (pos[0] - dist, pos[1])
        elif direction == 'U':
            pts = [(pos[0], y) for y in range(pos[1] + 1, pos[1] + dist + 1)]
            pos = (pos[0], pos[1] + dist)
        elif direction == 'D':
            pts = [(pos[0], y) for y in range(pos[1] - 1, pos[1] - dist - 1, -1)]
            pos = (pos[0], pos[1] - dist)

        for p in pts:
            steps += 1
            if p not in all_pts:
                step_count[p] = steps
            all_pts.add(p)

    return all_pts, step_count

points1, step_count1 = get_points(wire1)
points2, step_count2 = get_points(wire2)

common = points1 & points2
min_time = float("inf")

for pt in common:
    time = step_count1[pt] + step_count2[pt]
    if time > 0 and time < min_time:
        min_time = time

print(min_time)
