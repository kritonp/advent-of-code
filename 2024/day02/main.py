def monotonicity(list):
    increasing = list == sorted(list)
    decreasing = list == sorted(list, reverse = True)
    return increasing or decreasing


def check_safety(list_of_ints):
    isMonotonic = monotonicity(list_of_ints)

    max_diff, min_diff = float('-inf'), float('inf')
    for i in range(len(list_of_ints) - 1):
        diff = abs(list_of_ints[i + 1] - list_of_ints[i])
        max_diff = max(max_diff, diff)
        min_diff = min(min_diff, diff)

    if max_diff >= 1 and max_diff <= 3 and isMonotonic and min_diff>0:
        return True
    else:
        return False

def part_a(file_path):
    list_of_ints = []

    with open(file_path, 'r') as file:
        total_safe = 0
        for line in file:
            list_of_ints = list(map(int, line.split()))
            if check_safety(list_of_ints):
                total_safe += 1

    return total_safe


def part_b(file_path):
    list_of_ints=[]

    with open(file_path, 'r') as file:
        total_safe = 0
        for line in file:
            list_of_ints = list(map(int, line.split()))
            result = [list_of_ints[:i] + list_of_ints[i+1:] for i in range(len(list_of_ints))]
            isSafe=False
            for sublist in result:
                if check_safety(sublist):
                    isSafe = True
            if isSafe:
                total_safe+=1
        return total_safe


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()