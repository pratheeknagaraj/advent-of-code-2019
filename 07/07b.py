#!/usr/bin/python3

import copy
import itertools

with open('07_input', 'r') as f:
    lines = f.readlines()

program = [int(i) for i in lines[0].strip().split(',')]

def run(input_program, index, input_val_1 = None, input_val_2 = None):
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
            index += 2
            if mode_p1 == 0:
                output_val = program[pos]
                return output_val, program, index
            else:
                output_val = pos
                return output_val, program, index
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
            return None, None, None

def thruster_output(input_program, phase_setting):
    cur_input = 0
    phase_setting_list = phase_setting
    amplifier_count = len(phase_setting_list)
    programs = [input_program] * amplifier_count
    program_indicies = [0] * amplifier_count
    amplifier_index = 0

    last_thruster_val = None

    while True:
        if phase_setting_list:
            output_val, output_program, program_index = run(programs[amplifier_index], program_indicies[amplifier_index], phase_setting_list[0], cur_input)
            phase_setting_list = phase_setting_list[1:]
        else:
            output_val, output_program, program_index = run(programs[amplifier_index], program_indicies[amplifier_index], cur_input)

        if output_val == None:
            break

        cur_input = output_val
        programs[amplifier_index] = output_program
        program_indicies[amplifier_index] = program_index

        if amplifier_index == (amplifier_count - 1):
            last_thruster_val = cur_input
        
        amplifier_index += 1
        amplifier_index = amplifier_index % amplifier_count

    return last_thruster_val

def optimize(input_program):
    phases = [5,6,7,8,9]
    phase_settings = itertools.permutations(phases)

    max_val = float('-inf')
    max_setting = None

    for phase_setting in phase_settings:
        val = thruster_output(input_program, phase_setting)
        if val > max_val:
            max_val = val
            max_setting = phase_setting
    return max_val

# p1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# thruster_output(p1, [9,8,7,6,5])
# print(optimize(p1))

# p2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
# thruster_output(p2, [9,7,8,5,6])
# print(optimize(p2))

print(optimize(program))
