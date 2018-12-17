OPCODE = 0
A = 1
B = 2
C = 3
KEY = 0
VAL = 1

# each check function returns the possible opcodes that would change
# the registers accordingly
def check_math(before, after, inst, op, op_name):
    a = str(before[inst[A]])
    fits = []
    #r
    if after[inst[C]] == eval(a + op + str(before[inst[B]])):
        fits += 'r'
    #i
    if op_name == 'set':
        a = str(inst[A])
    if after[inst[C]] == eval(a + op + str(inst[B])):
        fits += 'i'
    return fits

def check_log(before, after, inst, op):
    fits = []
    #ri
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(inst[B])):
        fits.append('ri')
    #ir
    if after[inst[C]] == eval(str(inst[A]) + op + str(before[inst[B]])):
        fits.append('ir')
    #rr
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(before[inst[B]])):
        fits.append('rr')
    return fits

# returns True if the sample can be 3 or more opcodes
def process_sample(sample_lines):
    math_checks = {'add' : '+', 'mul' : '*', 'ban' : '&', 'bor': '|', 'set' : '#'}
    log_checks = {'gt' : '>', 'eq' : '=='}
    before = sample_lines[0].strip()
    before = eval(before[before.index(':') + 2:])
    after = sample_lines[2].strip()
    after = eval(after[after.index(':') + 2:])
    inst = sample_lines[1].strip().split()
    inst = [int(x) for x in inst]
    
    op_num = inst[OPCODE]
    possible_ops = []

    for op_name, op in math_checks.items():
        ops = check_math(before, after, inst, op, op_name)
        if ops:
            ops = [op_name + op_type for op_type in ops]
            possible_ops += ops

    for op_name, op in log_checks.items():
        ops = check_log(before, after, inst, op)
        if ops:
            ops = [op_name + op_type for op_type in ops]
            possible_ops += ops

    return [op_num, possible_ops]

def compile_opcodes():
    input_file = open("input1.txt", "r")
    samples = input_file.readlines()
    num_samples = 0
    opcodes = {}
    for i in range(0, len(samples), 4):
        opcode = process_sample(samples[i:i+3])

        if opcode[KEY] not in opcodes:
            opcodes[opcode[KEY]] = []

        current_codes = opcodes[opcode[KEY]]
        for op_type in opcode[VAL]:
            if op_type not in current_codes:
                current_codes.append(op_type)
    return opcodes

def determine_opcodes(opcodes):
    finalized = 0
    final_codes = {}
    while len(final_codes) < 15:
        for num, codes in opcodes.items():
            if len(codes) == 1:
                final_codes[num] = codes[0]
                code = codes[0]
                for num2, codes2 in opcodes.items():
                    if code in codes2:
                        codes2.remove(code)
                continue
            for code in codes:
                duplicate = False
                for num2, codes2 in opcodes.items():
                    if num != num2 and code in codes2:
                        duplicate = True
                if not duplicate:
                    final_codes[num] = code
                    opcodes[num] = []
                    break
    return final_codes

def eval_inst(registers, inst, opcodes):
    math = {'add' : '+', 'mul' : '*', 'ban' : '&', 'bor': '|', 'set' : '#'}
    log = {'gt' : '>', 'eq' : '=='}
    opcode = opcodes[inst[OPCODE]]
    is_math = opcode[:3] in math
    a = registers[inst[A]] if ((is_math and opcode != 'seti') or opcode[2] == 'r') else inst[A]
    b = registers[inst[B]] if opcode[3] == 'r' else inst[B]
    # math operation
    if is_math:
        registers[inst[C]] = eval(str(a) + math[opcode[:3]] + str(b))
    # logic operation
    else:
        registers[inst[C]] = 1 if eval(str(a) + log[opcode[:2]] + str(b)) else 0
    print(inst, opcode, registers)

def run_instructions(opcodes):
    input_file = open("input2.txt", "r")
    instructions = input_file.readlines()
    registers = [0] * 4
    for inst in instructions:
        inst = inst.strip().split()
        inst = [int(x) for x in inst]
        eval_inst(registers, inst, opcodes)
    return registers[0]

def main():
    opcodes = compile_opcodes()
    opcodes = determine_opcodes(opcodes)
    print(opcodes)
    print(run_instructions(opcodes))

if __name__== "__main__":
    main()
