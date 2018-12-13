# 20 gen - 3276

def calc_plants():
    input_file = open("input.txt", "r")
    plants = input_file.readline()
    plants = plants[plants.index(':') + 2:].strip()
    offset = 5
    base = ''
    plants = '.....' + plants + '.....'
    gens = 50000000000
    print(plants)

    for i in range(len(plants)):
        base += '.'

    rules = input_file.readlines()
    transform = {}

    for rule in rules:
        if '=' in rule:
            start = rule[:rule.index('=') - 1]
            end = rule[len(rule) - 2]
            transform[start] = end

    for day in range(gens):
        new_plants = base
        for i in range(2, len(plants) - 3):
            sublist = plants[i - 2:i + 3]
            if sublist in transform:
                new_plants = new_plants[:i] + transform[sublist] + new_plants[i + 1:]
        if '#' in new_plants[len(new_plants) - 5:]:
            append = 5 - len(new_plants) + new_plants.rfind('#')
            for i in range(append):
                new_plants += '.'
        if '#' in new_plants[:5]:
            new_off = 5 - new_plants.index('#')
            offset += new_off
            for i in range(new_off):
                new_plants = '.' + new_plants
        plants = new_plants


    sum = 0
    for i in range(len(plants)):
        real_ind = i - offset
        if plants[i] == '#':
            sum += real_ind

    return sum


def main():
    print(calc_plants())

if __name__== "__main__":
    main()
