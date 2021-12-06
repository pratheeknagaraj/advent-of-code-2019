#!/usr/bin/python3

import copy

with open('05_input', 'r') as f:
    lines = f.readlines()

program = [int(i) for i in lines[0].strip().split(',')]

def run(input_program, input_val = 5):
    index = 0
        
    program = copy.deepcopy(input_program)

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
            program[pos] = input_val
            index += 2
        elif inst == 4:
            pos = program[index + 1]
            if mode_p1 == 0:
                print(program[pos])
            else:
                print(pos)
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
            return program

# Tests

# p1 = [3,9,8,9,10,9,4,9,99,-1,8]
# p2 = [3,9,7,9,10,9,4,9,99,-1,8]
# p3 = [3,3,1108,-1,8,3,4,3,99]
# p4 = [3,3,1107,-1,8,3,4,3,99]
# p5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# p6 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
p7 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, \
      1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, \
      999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

# run(p1, 8)
# run(p1, 0)
# run(p2, 8)
# run(p2, 0)
# run(p3, 8)
# run(p3, 0)
# run(p4, 8)
# run(p4, 0)
# run(p5, 8)
# run(p5, 0)
# run(p6, 8)
# run(p6, 0)
# run(p7, 7)
# run(p7, 8)
# run(p7, 9)

res = run(program)
