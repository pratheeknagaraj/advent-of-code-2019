#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

grid = [[True if x == '#' else False for x in l.strip()] for l in lines]

rows = len(grid)
cols = len(grid[0])

asteroids = set()

for y in range(rows):
    for x in range(cols):
        if grid[y][x]:
            asteroids.add((x,y))

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

def detect_count(station_pos):
    count = 0

    for m in asteroids:
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
        for n in asteroids:
            if n in (station_pos, m):
                continue

            if on_line(slope, intercept, m, n):
                if interfering(station_pos, m, n):
                    valid = False
                    break

        if valid:
            count += 1

    return count

detection_count_map = {}
for s in asteroids:
    detection_count_map[s] = detect_count(s)

# print(max(detection_count_map.items(), key=lambda x: x[1]))
print(max(detection_count_map.values()))
    
