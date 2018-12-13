def calc_plants():
    input_file = open("input.txt", "r")
    plants = input_file.readline()
    plants = plants[plants.index(':') + 2:].strip()
    offset = 40
    base = ''
    plants = '........................................' + plants + '....................................'
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
    print(transform)

    for day in range(20):
        new_plants = base
        for i in range(2, len(plants) - 3):
            sublist = plants[i - 2:i + 3]
            if sublist in transform:
                new_plants = new_plants[:i] + transform[sublist] + new_plants[i + 1:]
        plants = new_plants
        print(plants)

    print(plants)

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
