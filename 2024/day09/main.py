def rearrange_disk(disk_map):
    disk = disk_map[:]
    while "." in disk:
        rightmost_index = len(disk) - 1 # Get the rightmost file block
        while disk[rightmost_index] == ".":
            rightmost_index -= 1

        leftmost_free_index = disk.index(".") # Get the leftmost free space

        if rightmost_index < leftmost_free_index:
            break

        disk[leftmost_free_index] = disk[rightmost_index] # Move the file block to the leftmost free space
        disk[rightmost_index] = "."

    return disk


def part_a(file_path):
    with open(file_path, "r") as file:
        input = file.read().strip()
    input_list = [int(char) for char in input]

    result = []
    current_id = 0
    pid = 0
    for size in input_list:
        size = int(size)
        if current_id % 2==0 or current_id==0:
            for _ in range(size):
                result.append(pid)
            pid+=1
        else:
            for _ in range(size):
                result.append(".")
        current_id += 1

    steps = rearrange_disk(result)
    checksum = 0
    for position, block in enumerate(steps):
        if block != '.':
            checksum += position * int(block)
    return checksum


def part_b(file_path):
    with open(file_path, "r") as file:
        input = file.read().strip()
    input_list = [int(char) for char in input]

    return 0


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()