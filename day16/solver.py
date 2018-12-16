A = 1
B = 2
C = 3

# each check function returns the number of possible opcodes that would change
# the registers accordingly
def check_add(before, after, inst):
    fits = 0
    #addi
    if after[inst[C]] == before[inst[A]] + before[inst[B]]:
        fits += 1
    #addr
    if after[inst[C]] == before[inst[A]] + inst[B]:
        fits += 1
    return fits

def check_mul(before, after, inst):
    fits = 0
    #muli
    if after[inst[C]] == before[inst[A]] * before[inst[B]]:
        fits += 1
    #mulr
    if after[inst[C]] == before[inst[A]] * inst[B]:
        fits += 1
    return fits

def check_ban(before, after, inst):
    fits = 0
    #bani
    if after[inst[C]] == before[inst[A]] & before[inst[B]]:
        fits += 1
    #banr
    if after[inst[C]] == before[inst[A]] & inst[B]:
        fits += 1
    return fits

def check_bor(before, after, inst):
    fits = 0
    #bori
    if after[inst[C]] == before[inst[A]] | before[inst[B]]:
        fits += 1
    #borr
    if after[inst[C]] == before[inst[A]] | inst[B]:
        fits += 1
    return fits

def check_set(before, after, inst):
    fits = 0
    #seti
    if after[inst[C]] == before[inst[A]]:
        fits += 1
    #setr
    if after[inst[C]] == inst[A]:
        fits += 1
    return fits

def check_gt(before, after, inst):
    fits = 0
    #gtri
    if after[inst[C]] == (before[inst[A]] > inst[B]):
        fits += 1
    #gtir
    if after[inst[C]] == (inst[A] > before[inst[B]]):
        fits += 1
    #gtrr
    if after[inst[C]] == (before[inst[A]] > before[inst[B]]):
        fits += 1
    return fits

def check_eq(before, after, inst):
    fits = 0
    #eqri
    if after[inst[C]] == (before[inst[A]] == inst[B]):
        fits += 1
    #eqir
    if after[inst[C]] == (inst[A] == before[inst[B]]):
        fits += 1
    #eqrr
    if after[inst[C]] == (before[inst[A]] == before[inst[B]]):
        fits += 1
    return fits

# returns True if the sample can be 3 or more opcodes
def process_sample(sample_lines):
    checks = [check_add, check_mul, check_ban, check_bor, check_set, check_gt,
              check_eq]
    before = sample_lines[0].strip()
    before = eval(before[before.index(':') + 2:])
    after = sample_lines[2].strip()
    after = eval(after[after.index(':') + 2:])
    inst = sample_lines[1].strip().split()
    inst = [int(x) for x in inst]
    
    num_ops = 0

    for check in checks:
        num_ops += check(before, after, inst)

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
