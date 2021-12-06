#!/usr/bin/python3

with open('05_input', 'r') as f:
    lines = f.readlines()

program = [int(i) for i in lines[0].strip().split(',')]

def run(program, input_val = 1):
    index = 0

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
        elif inst == 99:
            return program
        
# Tests

# p1 = [1002,4,3,4,33]
# p2 = [1101,100,-1,4,0]

# print(run(p1))
# print(run(p2))

res = run(program)
