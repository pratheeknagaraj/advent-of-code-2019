#!/usr/bin/python3

import numpy as np

with open('10_input', 'r') as f:
    lines = f.readlines()

grid = [[True if x == '#' else False for x in l.strip()] for l in lines]

rows = len(grid)
cols = len(grid[0])

meteors = set()

for y in range(rows):
    for x in range(cols):
        if grid[y][x]:
            meteors.add((x,y))

def on_line(slope, intercept, m, n):
    if slope == None:
        if m[0] == n[0]:
            return True
        return False
    if abs(n[1] - slope * n[0] - intercept) < 1e-6:
        return True
    return False

def interfering(a, b, n):
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])

    if min_x <= n[0] <= max_x and min_y <= n[1] <= max_y:
        return True
    return False

def detect_list(station_pos):
    detected = []

    for m in meteors:
        if m == station_pos:
            continue

        x1, y1 = station_pos
        x2, y2 = m

        if x1 != x2:
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
        else:
            slope = None
            intercept = None

        valid = True
        for n in meteors:
            if n in (station_pos, m):
                continue

            if on_line(slope, intercept, m, n):
                if interfering(station_pos, m, n):
                    valid = False
                    break

        if valid:
            detected.append(m)

    return detected

def order_rotationally(station, detected):
    def angle(d):
        # Add epsilonic value in delta to shift points into quadrant to get range [-PI, PI)
        delta = (station[0] - d[0] - 1e-2, d[1] - station[1])
        return np.arctan2(delta[0], delta[1])
    return sorted(detected, key=lambda x: angle(x))


# 267 asteroids can be detected from station, no need for multiple rotations (>200)
station = (26, 28) 
detected = detect_list(station)
rotational_order = order_rotationally(station, detected)
asteroid_200 = rotational_order[199]
val = asteroid_200[0] * 100 + asteroid_200[1]
print(val)
