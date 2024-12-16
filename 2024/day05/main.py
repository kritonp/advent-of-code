from collections import defaultdict


def get_input(file_path):
    part1, part2 = [], []
    with open(file_path, 'r') as file:
        is_second_part = False
        for line in file:
            if line.strip() == '':  # Split by empty line
                is_second_part = True
                continue
            if not is_second_part:
                part1.append(line.strip())
            else:
                part2.append([int(x) for x in line.strip().split(',')])
    return part1, part2


def is_update_in_order(rules, update):
    """
    Check if a given update is in order based on the rules.

    :param rules: A dictionary where keys are page numbers and values are lists of pages that must come after the key.
    :param update: A list of pages in the update to check.
    :return: Boolean indicating if the update is in order.
    """
    position = {page: idx for idx, page in enumerate(update)}
    for page, must_come_after in rules.items():
        # print(page, must_come_after)
        for after_page in must_come_after:
            # If both pages are in the update, ensure the order is correct
            if page in position and after_page in position:
                if position[page] > position[after_page]:

                    return False
    return True

def part_a(file_path):
    part1, part2 = get_input(file_path)
    part1_dict = defaultdict(list)

    for entry in part1:
        a, b = entry.split('|')
        part1_dict[int(a)].append(int(b))

    sum = 0
    for update in part2:
        if is_update_in_order(part1_dict, update):
            sum += update[len(update) // 2]
    return sum



def part_b(file_path):

    return 0


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()