def get_surroundings(plots, row, col):
    sur = []
    for new_row in range(max(row - 1, 0), min(row + 2, len(plots))):
        for new_col in range(max(col - 1, 0), min(col + 2, len(plots[row]))):
            if new_row != row or new_col != col:
                sur.append(plots[new_row][new_col])
    return sur

def new_value(plots, row, col):
    surroundings = get_surroundings(plots, row, col)
    cur_value = plots[row][col]
    if cur_value == '.':
        if surroundings.count('|') >= 3:
            return '|'
        return '.'
    elif cur_value == '|':
        if surroundings.count('#') >= 3:
            return '#'
        return '|'
    elif cur_value == '#' and surroundings.count('#') >= 1 and surroundings.count('|') >= 1:
        return '#'
    return '.'

def calc_lumber():
    input_file = open("input.txt", "r")
    plots = []
    mins = 10

    for line in input_file:
        plot_list = []
        for char in line.strip():
            plot_list.append(char)
        plots.append(plot_list)

    for minute in range(mins):
        new_plots = []
        for row in range(len(plots)):
            new_plots.append([])
            for col in range(len(plots[row])):
                new_plots[row].append(new_value(plots, row, col))
        plots = new_plots
        for plot in plots:
            print(*plot)

    woods = 0
    lumber = 0
    for plot_row in plots:
        woods += plot_row.count('|')
        lumber += plot_row.count('#')
    return woods * lumber


def main():
    print(calc_lumber())

if __name__== "__main__":
    main()
