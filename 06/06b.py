#!/usr/bin/python3

with open('06_input', 'r') as f:
    lines = f.readlines()

pairs = []
for l in lines:
    head, tail = l.strip().split(')')
    pairs.append((head, tail))

class Node:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

        self.orbit_count = None

root = Node('COM')

node_dict = {}

for p in pairs:
    head, tail = p
    if head not in node_dict:
        head_node = Node(head)
        node_dict[head] = head_node
    if tail not in node_dict:
        tail_node = Node(tail)
        node_dict[tail] = tail_node

    head_node, tail_node = node_dict[head], node_dict[tail]
    head_node.children.append(tail_node)
    tail_node.parent = head_node

def count_orbits(n):
    count = 0
    while n.parent != None:
        count += 1
        n = n.parent
        if n.orbit_count != None:
            count += n.orbit_count
            break
    return count

for n in node_dict.values():
    if n.orbit_count == None:
        orbits = count_orbits(n)
        n.orbit_count = orbits
    else:
        orbits = n.orbit_count

you_to_root = {}

you = node_dict['YOU']
san = node_dict['SAN']

cur = you
dist = 0
while True:
    parent = cur.parent
    if parent == None:
        break
    you_to_root[parent.name] = dist
    dist += 1
    cur = parent

cur = san
dist = 0
while True:
    parent = cur.parent
    if parent == None:
        break
    if parent.name in you_to_root:
        tot_dist = you_to_root[parent.name] + dist
        print(tot_dist)
        break
    dist += 1
    cur = parent

