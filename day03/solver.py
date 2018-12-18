import re

def slice_it():
    input_file = open("input.txt", "r")

    fabric = [['.' for i in range(1000)] for j in range(1000)]

    for line in input_file:
        split_line = re.split(' |,|:|x|\n', line)
        id = int(split_line[0][1:])
        start_x = int(split_line[2])
        start_y = int(split_line[3])
        width = int(split_line[5])
        height = int(split_line[6])

        for i in range(start_y, start_y + height):
            for j in range(start_x, start_x + width):
                if fabric[i][j] != '.':
                    fabric[i][j] = 'X'
                else:
                    fabric[i][j] = 'id'

    sum = 0
    for row in fabric:
        for inch in row:
            if inch == 'X':
                sum += 1

    return sum

def main():
    print(slice_it())

if __name__== "__main__":
    main()
