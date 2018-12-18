import re

def slice_it():
    input_file = open("input.txt", "r")

    fabric = [['.' for i in range(1000)] for j in range(1000)]
    valid = [1 for i in range(1338)]

    for line in input_file:
        split_line = re.split(' |,|:|x|\n', line)
        claim_id = int(split_line[0][1:])
        start_x = int(split_line[2])
        start_y = int(split_line[3])
        width = int(split_line[5])
        height = int(split_line[6])

        for i in range(start_y, start_y + height):
            for j in range(start_x, start_x + width):
                old_id = fabric[i][j]
                if old_id == 'X':
                    valid[claim_id] = 0
                elif old_id != '.':
                    old_id = int(old_id)
                    fabric[i][j] = 'X'
                    valid[claim_id] = 0
                    valid[old_id] = 0
                else:
                    fabric[i][j] = claim_id

    for i in range(1, len(valid)):
        if valid[i] == 1:
            return i

def main():
    print(slice_it())

if __name__== "__main__":
    main()
