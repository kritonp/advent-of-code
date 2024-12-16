from collections import defaultdict

def part_a(file_path):
    blinks = 25

    with open(file_path, "r") as file:
        int_list = [int(num) for num in file.read().split()]


    for _ in range(blinks):
        next_list = []
        for i in range(len(int_list)):
            if int_list[i] == 0:
                next_list.append(1)
            else:
                length = len(str(int_list[i]))
                if length % 2 == 0 and length > 1:
                    midpoint = len(str(int_list[i])) // 2
                    part1 = str(int_list[i])[:midpoint]  # First half
                    part2 = str(int_list[i])[midpoint:]  # Second half
                    next_list.append(int(part1))
                    next_list.append(int(part2))
                else:
                    next_list.append(int_list[i] * 2024)
        # print(next_list)
        int_list = next_list

    return len(int_list)


def part_b(file_path):
    blinks = 75
    with open(file_path, "r") as file:
        stones = defaultdict(int)
        for num in file.read().split():
            stones[int(num)] += 1


    for _ in range(blinks):
        next_stones = defaultdict(int)
        for value, count in stones.items():
            if value == 0:
                next_stones[1] += count
            else:
                length = len(str(value))
                if length % 2 == 0 and length > 1:
                    midpoint = length // 2
                    part1 = int(str(value)[:midpoint])
                    part2 = int(str(value)[midpoint:])
                    next_stones[part1] += count
                    next_stones[part2] += count
                else:
                    next_stones[value * 2024] += count
        stones = next_stones

    return sum(stones.values())


def main():
    print(part_a("input.txt"))
    print(part_b("input.txt"))


if __name__ == "__main__":
    main()
