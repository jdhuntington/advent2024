#!/usr/bin/env python3

import sys
import multiprocessing as mp
from itertools import islice


# 403,030,000

class Machine:
    def __init__(self, registers, instructions):
        self.registers = registers
        self.instruction_pointer = 0
        self.instructions = instructions
    
    def resolve_combo(self, combo):
        # There are two types of operands; each instruction specifies
        # the type of its operand. The value of a literal operand is
        # the operand itself. For example, the value of the literal
        # operand 7 is the number 7. The value of a combo operand can
        # be found as follows:

        # Combo operands 0 through 3 represent literal values 0 through 3.
        # Combo operand 4 represents the value of register A.
        # Combo operand 5 represents the value of register B.
        # Combo operand 6 represents the value of register C.
        # Combo operand 7 is reserved and will not appear in valid programs.

        if combo < 4:
            return combo
        elif combo == 4:
            return self.registers['A']
        elif combo == 5:
            return self.registers['B']
        elif combo == 6:
            return self.registers['C']
        else:
            raise ValueError(f'Invalid combo operand {combo}')


    def adv(self, operand):
        # The adv instruction (opcode 0) performs division. The
        # numerator is the value in the A register. The denominator is
        # found by raising 2 to the power of the instruction's combo
        # operand. (So, an operand of 2 would divide A by 4 (2^2); an
        # operand of 5 would divide A by 2^B.)
        # The result of the division operation is truncated to an integer and then written to the A register.

        self.registers['A'] //= 2 ** self.resolve_combo(operand)

    def out(self, operand, output):
        # The out instruction (opcode 5) calculates the value of its
        # combo operand modulo 8, then outputs that value. (If a
        # program outputs multiple values, they are separated by
        # commas.)
        output.append(self.resolve_combo(operand) % 8)

    def jnz(self, operand):
        # The jnz instruction (opcode 3) does nothing if the A
        # register is 0. However, if the A register is not zero, it
        # jumps by setting the instruction pointer to the value of its
        # literal operand; if this instruction jumps, the instruction
        # pointer is not increased by 2 after this instruction.
        if self.registers['A'] != 0:
            self.instruction_pointer = operand
    
    def bst(self, operand):
        # The bst instruction (opcode 2) calculates the value of its
        # combo operand modulo 8 (thereby keeping only its lowest 3
        # bits), then writes that value to the B register.
        self.registers['B'] = self.resolve_combo(operand) % 8

    def bxl(self, operand):
        # The bxl instruction (opcode 1) calculates the bitwise XOR of
        # register B and the instruction's literal operand, then
        # stores the result in register B.
        self.registers['B'] ^= operand

    def cdv(self, operand):
        # The cdv instruction (opcode 7) works exactly like the adv
        # instruction except that the result is stored in the C
        # register. (The numerator is still read from the A register.)
        numerator = self.registers['A']
        denominator = 2 ** self.resolve_combo(operand)  
        self.registers['C'] = numerator // denominator

    def bxc(self, operand):
        # The bxc instruction (opcode 4) calculates the bitwise XOR of
        # register B and register C, then stores the result in
        # register B. (For legacy reasons, this instruction reads an
        # operand but ignores it.)
        self.registers['B'] ^= self.registers['C']

    def run(self):
        output = []
        while self.instruction_pointer < len(self.instructions) - 1:
            opcode = self.instructions[self.instruction_pointer]
            operand = self.instructions[self.instruction_pointer + 1]
            self.instruction_pointer += 2
            if opcode == 0:
                self.adv(operand)
            elif opcode == 1:
                self.bxl(operand)
            elif opcode == 2:
                self.bst(operand)
            elif opcode == 3:
                self.jnz(operand)
            elif opcode == 4:
                self.bxc(operand)
            elif opcode == 5:
                self.out(operand, output)
            elif opcode == 6:
                self.bdv(operand)
            elif opcode == 7:
                self.cdv(operand)
            else:
                raise ValueError(f'Unknown opcode {opcode}')
        return output

def get_input():
    return sys.stdin.read()

def parse_program(input_text):
    registers_text, program_text = input_text.strip().split('\n\nProgram: ')
    
    registers = {}
    for line in registers_text.split('\n'):
        register, value = line.split(': ')
        register_name = register.split()[-1]
        registers[register_name] = int(value)
    
    instructions = [int(x) for x in program_text.split(',')]
    
    return registers, instructions

def find_answer(original_registers, instructions, a = 0, index = 0):
    registers = dict(original_registers)
    registers['A'] = a
    machine = Machine(registers, instructions)
    result = machine.run()
    if result == instructions:
        print(a)
    elif result == instructions[-index:] or index == 0:
        for n in range(8):
            find_answer(original_registers, instructions, 8 * a + n, index + 1)


if __name__ == "__main__":
    registers, instructions = parse_program(get_input())
    answered = False
    find_answer(registers, instructions)