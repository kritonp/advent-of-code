import pandas as pd
import numpy as np
from scipy.ndimage import label


def add_padding(df):
    df['end'] = 0 # Add new column at the end
    df.insert(0, "start", 0, True) # add new column at the begging

    # Add new row at top
    new_row = pd.DataFrame([np.zeros(df.shape[1], dtype=int)], columns=df.columns)
    df = pd.concat([new_row, df], ignore_index=True)

    df.loc[len(df)] = 0 # Add new row at the end
    return df

def part_a(file):
    df = pd.DataFrame([list(line.strip()) for line in open(file, 'r')])
    unique_values = df.stack().unique()

    df = add_padding(df)

    total_price = 0
    for elem in unique_values:
        binary_df = (df == elem).astype(int)

        labeled_matrix, num_features = label(binary_df)


        # Extract each block as a separate DataFrame
        # Plants of the same type can appear in multiple separate regions,
        # and regions can even appear within other regions.
        blocks = {}
        for i in range(1, num_features + 1):
            block = (labeled_matrix == i).astype(int)
            blocks[i] = pd.DataFrame(block)


        for _, block in blocks.items():
            # print(block)
            adjacent_zeros = np.zeros_like(block, dtype=int)

            # Check for zeros in each direction
            up = block.shift(-1, axis=0).fillna(0)
            down = block.shift(1, axis=0).fillna(0)
            left = block.shift(-1, axis=1).fillna(0)
            right = block.shift(1, axis=1).fillna(0)

            adjacent_zeros = (1 - up) + (1 - down) + (1 - left) + (1 - right) # count zeros adjacent to 1s

            adjacent_zeros = adjacent_zeros * block # Keep counts only for cells with 1s

            adjacent_zeros_df = pd.DataFrame(adjacent_zeros, columns=block.columns)
            adjacent_zeros_df = adjacent_zeros_df.astype(int)
            area = (block == 1).sum().sum()
            block_price = area*adjacent_zeros_df.sum().sum()
            # print('area= ', area)
            # print('perimeter= ', adjacent_zeros_df.sum().sum())
            # print('block_price= ', block_price)
            total_price += block_price
    return total_price


def part_b(file_path):
    return 0


def main():
    print(part_a('input.txt'))
    print(part_b("input.txt"))


if __name__ == "__main__":
    main()
