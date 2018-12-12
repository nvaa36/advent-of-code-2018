input_file = open("input.txt", "r")

freq = 0
for line in input_file:
    operator = line[0]
    number = int(line[1:])
    if operator == '-':
        freq -= number
    else:
        freq += number
print(freq)
