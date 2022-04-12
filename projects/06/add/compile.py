import re
from sys import argv

script, in_file, out_file = argv

# From file to instruction list
instruction_list = open(in_file,"r")
lines = instruction_list.read().split('\n')

# Parser
C_COMMAND = '(\w+)[=;]?([-!]?\w+[+-|&]?\w*)'
A_COMMAND = '@(\w+)'
L_COMMAND = '\((\w+)\)'
for line in lines:
    if re.match(C_COMMAND,line):
        print(f"{(re.match(C_COMMAND,line).group(1),re.match(C_COMMAND,line).group(2))}")


    elif re.match(A_COMMAND,line):
        print(f"{(re.match(A_COMMAND,line).group(1))}")
        print("\t A Instruction is: ");
    elif re.match(L_COMMAND,line):
        print(f"{(re.match(L_COMMAND,line).group(1))}")
        print("\t L Instruction is: ");
    else:
        print("not match")

# Convert to Binary
def codeA(symbol):
    pass
def codeL(symbol):
    pass
def codeC(dest, comp, jump):
    COMP_MAP = {
        '0': '101010',
        '1': '111111',
        '-1': '111010',
        'D': '001100',
        'A': '110000', 'M': '110000',
        '!D': '001101',
        '!A': '110001', '!M': '110001',
        '-D': '001111',
        '-A': '110011', '-M': '110011',
        'D+1': '011111',
        'A+1': '110111', 'M+1': '110111',
        'D-1': '001110',
        'A-1': '110010', 'M-1': '110010',
        'D+A': '000010', 'D+M': '000010',
        'D-A': '010011', 'D-M': '010011',
        'A-D': '000111', 'M-D': '000111',
        'D&A': '000000', 'D&M': '000000',
        'D|A': '010101', 'D|M': '010101',
    }

    JUMP_MAP = {'JGT':'001', 'JEQ':'010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
    DEST_MAP = {'M': '001', 'D': '010', 'MD':'011', 'A':'100', 'AM': '101', 'AD': '110', 'AMD': '111'}




