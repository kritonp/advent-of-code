def part_a(file_path):
    list1, list2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            col1, col2 = line.strip().split()
            list1.append(int(col1))
            list2.append(int(col2))

    list1.sort()
    list2.sort()

    total_distance = sum([abs(a_i - b_i) for a_i, b_i in zip(list1, list2)])
    return total_distance


def part_b(file_path):
    list1, list2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            col1, col2 = line.strip().split()
            list1.append(int(col1))
            list2.append(int(col2))

    similarity_score = 0
    for i in list1:
        similarity_score += i*list2.count(i)
    return similarity_score


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()