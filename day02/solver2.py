def get_id():
    input_file = open("input.txt", "r")

    ids = []

    for line in input_file:
        line_len = len(line)

        for old_id in ids:
            num_same = 0
            for i in range(line_len):
                if old_id[i] == line[i]:
                    num_same +=1
            if num_same == line_len - 1:
                return (old_id, line)

        ids.append(line)

def main():
    (l1, l2) = get_id()

    for i in range(len(l1)):
        if l1[i] == l2[i]:
            print(l1[i], end='')


if __name__== "__main__":
    main()
