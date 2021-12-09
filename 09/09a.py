#!/usr/bin/python3

import copy

with open('09_input', 'r') as f:
    lines = f.readlines()

program = [int(i) for i in lines[0].strip().split(',')]

def run(input_program, input_val = None):
    index = 0
    relative_base = 0

    program = copy.deepcopy(input_program)

    def get(index):
        if len(program) <= index:
            extend_count = index - len(program) + 1
            program.extend([0] * extend_count)
        return program[index]

    def put(index, val):
        if len(program) <= index:
            extend_count = index - len(program) + 1
            program.extend([0] * extend_count)
        program[index] = val

    def mode_val(mode, val):
        if mode == 0:
            return get(val)
        if mode == 1:
            return val
        if mode == 2:
            return get(relative_base + val)

    def mode_pos(mode, pos):
        if mode == 2:
            return relative_base + pos
        if mode == 1:
            raise Exception("Cannot write using immediate mode")
        return pos

    while True:
        opcode = program[index]
        inst = opcode % 100
        mode_p1 = (opcode // 100) % 10
        mode_p2 = (opcode // 1000) % 10
        mode_p3 = (opcode // 10000) % 10
        
        if inst == 1:
            val1 = get(index + 1)
            val1 = mode_val(mode_p1, val1)
            val2 = get(index + 2)
            val2 = mode_val(mode_p2, val2)
            pos = get(index + 3)
            pos = mode_pos(mode_p3, pos)
            put(pos, val1 + val2)
            index += 4
        elif inst == 2:
            val1 = get(index + 1)
            val1 = mode_val(mode_p1, val1)
            val2 = get(index + 2)
            val2 = mode_val(mode_p2, val2)
            pos = get(index + 3)
            pos = mode_pos(mode_p3, pos)
            put(pos, val1 * val2)
            index += 4
        elif inst == 3:
            pos = get(index + 1)
            pos = mode_pos(mode_p1, pos)
            put(pos, input_val)
            index += 2
        elif inst == 4:
            pos = get(index + 1)
            val = mode_val(mode_p1, pos)
            print(val)
            index += 2
        elif inst == 5:
            val = get(index + 1)
            val = mode_val(mode_p1, val)
            if val != 0:
                pos = get(index + 2)
                pos = mode_val(mode_p2, pos)
                index = pos
            else:
                index += 3
        elif inst == 6:
            val = get(index + 1)
            val = mode_val(mode_p1, val)
            if val == 0:
                pos = get(index + 2)
                pos = mode_val(mode_p2, pos)
                index = pos
            else:
                index += 3
        elif inst == 7:
            val1 = get(index + 1)
            val1 = mode_val(mode_p1, val1)
            val2 = get(index + 2)
            val2 = mode_val(mode_p2, val2)
            pos = get(index + 3)
            pos = mode_pos(mode_p3, pos)
            if val1 < val2:
                put(pos, 1)
            else:
                put(pos, 0)
            index += 4
        elif inst == 8:
            val1 = get(index + 1)
            val1 = mode_val(mode_p1, val1)
            val2 = get(index + 2)
            val2 = mode_val(mode_p2, val2)
            pos = get(index + 3)
            pos = mode_pos(mode_p3, pos)
            if val1 == val2:
                put(pos, 1)
            else:
                put(pos, 0)
            index += 4
        elif inst == 9:
            val = get(index + 1)
            val = mode_val(mode_p1, val)
            relative_base += val
            index += 2
        elif inst == 99:
            return program

# Tests

# p1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# p2 = [1102,34915192,34915192,7,4,7,99,0]
# p3 = [104,1125899906842624,99]

# run(p1)
# run(p2)
# run(p3)

res = run(program, 1)
