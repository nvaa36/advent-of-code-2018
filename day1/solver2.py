def calc_freq():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    frequencies = [0]
    freq = 0
    while True:
        for line in lines:
            operator = line[0]
            number = int(line[1:])
            if operator == '-':
                freq -= number
            else:
                freq += number
            if freq in frequencies:
                return freq
            frequencies.append(freq)

def main():
    print(calc_freq())

if __name__== "__main__":
    main()
