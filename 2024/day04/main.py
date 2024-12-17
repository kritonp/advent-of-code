def add_padding(matrix):
    """"
        Add a padding of 4 around matrix
    """
    cols = len(matrix[0])

    padded_matrix = [['.'] * (cols + 8) for _ in range(4)]  # Top padding

    for row in matrix:
        padded_matrix.append(['.'] * 4 + row + ['.'] * 4)

    padded_matrix.extend([['.'] * (cols + 8) for _ in range(4)])

    return padded_matrix


def find_key_positions(matrix, letter):
    positions = []
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == letter:
                positions.append((row_idx, col_idx))
    return positions



def count_keywords(matrix, position):
    """
    Counts the occurrences of the target keywords ('XMAS' and 'SAMX')
    in all directions from a given position in the 2D matrix.
    """
    keywords = ['XMAS', 'SAMX']
    count = 0
    row, col = position

    def contains_keyword(lst):
        word = ''.join(lst)
        return any(keyword in word for keyword in keywords)

    directions = {
        "row_right": matrix[row][col:col+4],  # Right (→)
        "row_left": matrix[row][col-3:col+1],  # Left (←)
        "col_down": [matrix[r][col] for r in range(row, row+4)],  # Down (↓)
        "col_up": [matrix[r][col] for r in range(row, row-4, -1)],  # Up (↑)
        "diag_down_right": [matrix[row+i][col+i] for i in range(4)],  # Diagonal ↘
        "diag_up_left": [matrix[row-i][col-i] for i in range(4)],  # Diagonal ↖
        "diag_up_right": [matrix[row-i][col+i] for i in range(4)],  # Diagonal ↗
        "diag_down_left": [matrix[row+i][col-i] for i in range(4)]   # Diagonal ↙
    }

    for _, chars in directions.items():
        if contains_keyword(chars):
            count += 1
    return count


def part_a(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(line.strip()) for line in file.readlines()]

    matrix = add_padding(matrix)
    positions = find_key_positions(matrix, 'X') # Get all starting positions
    total = 0
    for pos in positions:
        total += count_keywords(matrix, pos)
    return total



def part_b(file_path):
    def fetch_diagonals(matrix, row, col, directions):
        """Fetch values from diagonally adjacent positions."""
        values = []
        rows, cols = len(matrix), len(matrix[0])
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                values.append(matrix[new_row][new_col])
        return values

    with open(file_path, 'r') as file:
        matrix = [list(line.strip()) for line in file.readlines()]

    matrix = add_padding(matrix)
    positions = find_key_positions(matrix, 'A')

    diagonals_partA = [(-1, -1), (1, 1)]  # Top-left, Bottom-right
    diagonals_partB = [(-1, 1), (1, -1)]  # Top-right, Bottom-left
    total = 0
    for position in positions:
        row, col = position

        diagonals_partA_values = fetch_diagonals(matrix, row, col, diagonals_partA)
        diagonals_partB_values = fetch_diagonals(matrix, row, col, diagonals_partB)

        partA_has_M_and_S = 'M' in diagonals_partA_values and 'S' in diagonals_partA_values
        partB_has_M_and_S = 'M' in diagonals_partB_values and 'S' in diagonals_partB_values

        if partA_has_M_and_S and partB_has_M_and_S:
            total += 1

    return total


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()