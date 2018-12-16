OPCODE = 0
A = 1
B = 2
C = 3
KEY = 0
VAL = 1

# each check function returns the possible opcodes that would change
# the registers accordingly
def check_math(before, after, inst, op):
    fits = []
    #i
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(before[inst[B]])):
        fits += 'i'
    #r
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(inst[B])):
        fits += 'r'
    return fits

def check_log(before, after, inst, op):
    fits = []
    #ri
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(inst[B])):
        fits += 'ri'
    #ir
    if after[inst[C]] == eval(str(inst[A]) + op + str(before[inst[B]])):
        fits += 'ir'
    #rr
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(before[inst[B]])):
        fits += 'rr'
    return fits

# returns True if the sample can be 3 or more opcodes
def process_sample(sample_lines):
    math_checks = {'add' : '+', 'mul' : '*', 'ban' : '&', 'bor': '|'}
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
        if ((ops = check_math(before, after, inst, op))):
            ops = [op_name + op_type for op_type in ops]
            possible_ops += ops

    for op_name, op in log_checks.items():
        if ((ops = check_log(before, after, inst, op))):
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
        if opcode[KEY] in opcodes:
            opcodes[opcode[KEY]] += opcode[VAL]
        else:
            opcodes[opcode[KEY]] = opcode[VAL]
    return opcodes

def run_instructions(opcodes):
    return 1

def main():
    opcodes = compile_opcodes()
    print(run_instructions(opcodes))

if __name__== "__main__":
    main()
