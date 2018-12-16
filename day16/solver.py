A = 1
B = 2
C = 3

# 529

# each check function returns the number of possible opcodes that would change
# the registers accordingly
def check_math(before, after, inst, op):
    fits = 0
    #i
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(before[inst[B]])):
        fits += 1
    #r
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(inst[B])):
        fits += 1
    return fits

def check_log(before, after, inst, op):
    fits = 0
    #ri
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(inst[B])):
        fits += 1
    #ir
    if after[inst[C]] == eval(str(inst[A]) + op + str(before[inst[B]])):
        fits += 1
    #rr
    if after[inst[C]] == eval(str(before[inst[A]]) + op + str(before[inst[B]])):
        fits += 1
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
    
    num_ops = 0

    for op_name, op in math_checks.items():
        num_ops += check_math(before, after, inst, op)

    for op_name, op in log_checks.items():
        num_ops += check_log(before, after, inst, op)

    if num_ops >= 3:
        return True
    return False

def check_opcodes():
    input_file = open("input1.txt", "r")
    samples = input_file.readlines()
    num_samples = 0
    for i in range(0, len(samples), 4):
        if process_sample(samples[i:i+3]):
            num_samples += 1
    return num_samples


def main():
    print(check_opcodes())

if __name__== "__main__":
    main()
