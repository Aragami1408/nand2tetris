import re
from sys import argv

script, in_file = argv

# From file to instruction list
instruction_list = open(in_file,"r")
lines = instruction_list.read().split('\n')

# CONSTANTS
C_COMMAND = '(\w+)[=;]?([-!]?\w+[+-|&]?\w*)'
A_COMMAND = '@(\w+)'
L_COMMAND = '\((\w+)\)'

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

JUMP_MAP = {'JGT':'001', 'JEQ':'010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111', '': '000'}
DEST_MAP = {'M': '001', 'D': '010', 'MD':'011', 'A':'100', 'AM': '101', 'AD': '110', 'AMD': '111', '': '000'}

sym_map = { 
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5,
    'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
    'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SCREEN': 16384,
    'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4
}
var_map = {}
label_map = {}

# Convert to Binary
def codeA(symbol):
    if symbol.isnumeric():
        return '0' + '{0:015b}'.format(int(symbol))
    else:
        if symbol in sym_map:
            return '=' + '{0:015b}'.format(sym_map[symbol])
        else:
            var_map[symbol] = 16 + len(var_map)
            sym_map.update(var_map)
        
def codeL(symbol):
    pass
def codeC(dest, comp, jump):
    code_dest = DEST_MAP[dest]
    code_comp = COMP_MAP[comp]
    code_jump = JUMP_MAP[jump]

    return '111' + ('1' if 'M' in comp else '0') + code_comp + code_dest + code_jump

# Parser
for line in lines:
    if re.match(C_COMMAND,line):
        group1 = re.match(C_COMMAND,line).group(1)
        group2 = re.match(C_COMMAND,line).group(2)
        if group2 == 'JGT' or group2 == 'JEQ' or group2 == 'JGE' or group2 == 'JLT' or group2 == 'JNE' or group2 == 'JLE' or group2 == 'JMP': 
            print(f"\t C instruction (comp,jump) is: {codeC('',group1,group2)}")
        else:
            print(f"\t C instruction (dest,comp) is: {codeC(group1,group2,'')}")
    elif re.match(A_COMMAND,line):
        print(f"\t A Instruction is: {codeA(re.match(A_COMMAND,line).group(1))}");
    elif re.match(L_COMMAND,line):
        print("\t L Instruction is: ");
    else:
        print("not match")




