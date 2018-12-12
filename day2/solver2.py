input_file = open("input.txt", "r")

letter_freq = [0] * 256
twos = 0
threes = 0

def get_id():
    for line in input_file:
        for letter in line:
            letter_freq[ord(letter)] += 1
        if 2 in letter_freq:
            twos += 1
        if 3 in letter_freq:
            threes += 1
        letter_freq = [0] * 256

print(twos * threes)

def main():
    print(get_id())

if __name__== "__main__":
    main()
