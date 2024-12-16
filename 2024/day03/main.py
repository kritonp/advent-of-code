import re

def part_a(file_path):
    with open(file_path, 'r') as file:
        total_sum = 0
        for line in file:
            list_of_muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
            sum = 0
            for mul in list_of_muls:
                x1, x2 = re.findall(r'\b\d+\b', mul)
                sum+=int(x1)*int(x2)
            total_sum += sum
    return total_sum


def split_cmds(line):
    split_pattern = re.compile(r"(don't\(\)|do\(\))")
    split_lines = split_pattern.split(line)

    result = []
    buffer = ""
    for part in split_lines:
        if part in ["don't()", "do()"]:
            if buffer:
                result.append(buffer)
                buffer = ""
            buffer = part
        else:
            if buffer:
                result.append(buffer + part)
                buffer = ""
            else:
                result.append(part)
    return result


def part_b(file_path):
    with open(file_path, 'r') as file:
        concatenated_lines = ''.join(line.strip() for line in file)

    total_sum = 0
    for cmd in split_cmds(concatenated_lines):
        if cmd.startswith("don't()"):
            continue

        list_of_muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", cmd)
        cmd_sum = sum(
            int(x1) * int(x2)
            for x1, x2 in (re.findall(r"\b\d+\b", mul) for mul in list_of_muls)
        )

        total_sum += cmd_sum

    return total_sum


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()