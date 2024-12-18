def get_input(file_path):
    positions = []
    velocities = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                p = tuple(map(int, parts[0].split('=')[1].split(',')))
                v = tuple(map(int, parts[1].split('=')[1].split(',')))
                positions.append(p)
                velocities.append(v)
    return positions, velocities


def part_a(file_path):
    positions, velocities = get_input(file_path)

    width, height = 101, 103
    t=100
    final_pos = []
    for pos, vel in zip(positions, velocities):
        px, py = pos
        vx, vy = vel
        x = (px + vx * t) % width
        y = (py + vy * t) % height
        final_pos.append((x,y))


    quadrant_a, quadrant_b, quadrant_c, quadrant_d = 0, 0, 0, 0
    for pos in final_pos:
        x, y = pos
        if x<width//2 and y<height//2:
            quadrant_a+=1
        if x>width//2 and y<height//2:
            quadrant_b+=1
        if x<width//2 and y>height//2:
            quadrant_c+=1
        if x>width//2 and y>height//2:
            quadrant_d+=1

    return quadrant_a*quadrant_b*quadrant_c*quadrant_d


def part_b(file_path):
    positions, velocities = get_input(file_path)

    width, height = 101, 103
    for t in range(7_000):
        print(t)
        final_pos = []
        for pos, vel in zip(positions, velocities):
            px, py = pos
            vx, vy = vel
            x = (px + vx * t) % width
            y = (py + vy * t) % height
            final_pos.append((x,y))


        # Print all pattern and search for the tree
        matrix = [['.' for _ in range(height)] for _ in range(width)]
        for x, y in final_pos:
            matrix[x][y] = '#'
        for row in matrix:
            print("".join(map(str, row)))
        print()
        print()
    return 0


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()