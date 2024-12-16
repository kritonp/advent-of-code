def get_input(file_path):
    import re

    with open(file_path, 'r') as file:
        input_text = file.read()

    blocks = input_text.strip().split("\n\n")

    result = []
    for block in blocks:
        button_a_match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", block)
        button_a_x, button_a_y = map(int, button_a_match.groups()) if button_a_match else (None, None)

        button_b_match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", block)
        button_b_x, button_b_y = map(int, button_b_match.groups()) if button_b_match else (None, None)

        prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", block)
        prize_x, prize_y = map(int, prize_match.groups()) if prize_match else (None, None)

        result.append(
            {
                "Button A": {"X": button_a_x, "Y": button_a_y},
                "Button B": {"X": button_b_x, "Y": button_b_y},
                "Prize": {"X": prize_x, "Y": prize_y}
            }
        )

    return result



def part_a(file_path):
    input_data = get_input(file_path)
    cost_button_a, cost_button_b = 3 , 1
    total_button_a, total_button_b = 0, 0
    for game in input_data:
        # print(game)

        button_a_x, button_a_y = game['Button A']['X'], game['Button A']['Y']
        button_b_x, button_b_y = game['Button B']['X'], game['Button B']['Y']
        sol_x, sol_y = game['Prize']['X'], game['Prize']['Y']
        foundsol=False
        for i in range(100):
            for j in range(100):
                if (i*button_a_x + j*button_b_x==sol_x) and (i*button_a_y + j*button_b_y==sol_y):
                    # print(i,j)
                    total_button_a+=i
                    total_button_b+=j
                    foundsol=False
                    break
            if foundsol:
                break

    return cost_button_a*total_button_a + cost_button_b*total_button_b




def part_b(file_path):



    return 0


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()