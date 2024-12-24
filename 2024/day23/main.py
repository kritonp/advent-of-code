import networkx as nx

def part_a(file_path):
    G = nx.read_edgelist(file_path, delimiter='-')
    count = 0
    for clq in nx.clique.enumerate_all_cliques(G):
        if len(clq) == 3:
            tFound = False
            for elem in clq:
                if elem.startswith('t'):
                    tFound = True
            if tFound:
                count+=1
    return count


def part_b(file_path):
    G = nx.read_edgelist(file_path, delimiter='-')
    max_clq = max(nx.clique.enumerate_all_cliques(G), key=len)
    return ",".join(sorted(max_clq))


def main():
    print(part_a('input.txt'))
    print(part_b('input.txt'))


if __name__ == "__main__":
    main()