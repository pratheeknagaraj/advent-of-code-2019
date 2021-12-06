#!/usr/bin/python3

import copy

with open('02_input', 'r') as f:
    lines = f.readlines()

program = [int(i) for i in lines[0].strip().split(',')]

program[1] = 12
program[2] = 2

def run(program):
    index = 0

    while True:
        inst = program[index]
        if inst == 1:
            val1 = program[program[index + 1]]
            val2 = program[program[index + 2]]
            pos = program[index + 3]
            program[pos] = val1 + val2
        elif inst == 2:
            val1 = program[program[index + 1]]
            val2 = program[program[index + 2]]
            pos = program[index + 3]
            program[pos] = val1 * val2
        elif inst == 99:
            return program
        
        index += 4

def stage(program, noun, verb):
    p = copy.deepcopy(program)
    p[1] = noun
    p[2] = verb
    return p

# Tests

# p1 = [1,0,0,0,99]
# p2 = [2,3,0,3,99]
# p3 = [2,4,4,5,99,0]
# p4 = [1,1,1,4,99,5,6,0,99]

# print(run(p1))
# print(run(p2))
# print(run(p3))
# print(run(p4))

complete = False

for noun in range(0, 100):
    for verb in range(0, 100):
        res = run(stage(program, noun, verb))
        if res[0] == 19690720:
            val = 100 * noun + verb
            print(val)
            complete = True
            break
    if complete:
        break

