#!/usr/bin/python3

import copy
import itertools

with open('07_input', 'r') as f:
    lines = f.readlines()

program = [int(i) for i in lines[0].strip().split(',')]

def run(input_program, input_val_1 = None, input_val_2 = None):
    index = 0

    input_vals = [input_val_1, input_val_2]

    program = copy.deepcopy(input_program)

    output_val = None

    while True:
        opcode = program[index]
        inst = opcode % 100
        mode_p1 = (opcode // 100) % 10
        mode_p2 = (opcode // 1000) % 10
        mode_p3 = (opcode // 10000) % 10

        if inst == 1:
            val1 = program[index + 1]
            if mode_p1 == 0:
                val1 = program[val1]
            val2 = program[index + 2]
            if mode_p2 == 0:
                val2 = program[val2]
            pos = program[index + 3]
            program[pos] = val1 + val2
            index += 4
        elif inst == 2:
            val1 = program[index + 1]
            if mode_p1 == 0:
                val1 = program[val1]
            val2 = program[index + 2]
            if mode_p2 == 0:
                val2 = program[val2]
            pos = program[index + 3]
            program[pos] = val1 * val2
            index += 4
        elif inst == 3:
            pos = program[index + 1]
            program[pos] = input_vals[0]
            input_vals = input_vals[1:]
            index += 2
        elif inst == 4:
            pos = program[index + 1]
            if mode_p1 == 0:
                output_val = program[pos]
            else:
                output_val = pos
            index += 2
        elif inst == 5:
            val = program[index + 1]
            if mode_p1 == 0:
                val = program[val]
            if val != 0:
                pos = program[index + 2]
                if mode_p2 == 0:
                    pos = program[pos]
                index = pos
            else:
                index += 3
        elif inst == 6:
            val = program[index + 1]
            if mode_p1 == 0:
                val = program[val]
            if val == 0:
                pos = program[index + 2]
                if mode_p2 == 0:
                    pos = program[pos]
                index = pos
            else:
                index += 3
        elif inst == 7:
            val1 = program[index + 1]
            if mode_p1 == 0:
                val1 = program[val1]
            val2 = program[index + 2]
            if mode_p2 == 0:
                val2 = program[val2]
            pos = program[index + 3]
            if val1 < val2:
                program[pos] = 1
            else:
                program[pos] = 0
            index += 4
        elif inst == 8:
            val1 = program[index + 1]
            if mode_p1 == 0:
                val1 = program[val1]
            val2 = program[index + 2]
            if mode_p2 == 0:
                val2 = program[val2]
            pos = program[index + 3]
            if val1 == val2:
                program[pos] = 1
            else:
                program[pos] = 0
            index += 4
        elif inst == 99:
            return output_val

def thruster_output(input_program, phase_setting):
    cur_input = 0
    for phase_val in phase_setting:
        cur_input = run(input_program, phase_val, cur_input)
    return cur_input

def optimize(input_program):
    phases = [0,1,2,3,4]
    phase_settings = itertools.permutations(phases)

    max_val = float('-inf')
    max_setting = None

    for phase_setting in phase_settings:
        val = thruster_output(input_program, phase_setting)
        if val > max_val:
            max_val = val
            max_setting = phase_setting
    return max_val

# p1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# print(optimize(p1))
# p2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# print(optimize(p2))
# p3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# print(optimize(p3))

print(optimize(program))
