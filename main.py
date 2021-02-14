import torch
from time import sleep

def get_metadata(paper: int) -> dict:
    path = f'cit-HepTh-abstracts/{dates[paper].split("-")[0]}/{paper}.abs'
    try:
        with open(path, 'r') as f:
            line = f.readline()

            metadata = {}
            while line:
                print(line)
                if ':' in line:
                    metadata[line.split(":")[0]] = "".join(line.split(":")[1:])
                line = f.readline()

            return metadata
    except FileNotFoundError:
        print("FileNotFoundError: ", path)
        return {}

if __name__ == "__main__":
    nodes = []
    dates = {}
    with open("cit-HepTh-dates.txt", 'r') as f:
        line = f.readline()

        while line:
            if line[0] == "#":
                line = f.readline()
                continue

            if len(line.split(" ")) > 1:
                node = line.split(" ")[0]
                date = line.split(" ")[1]
            else:
                node = line.split("\t")[0]
                date = line.split("\t")[1]
            date = date.strip()
            node = int(node.strip())
            nodes.append(node)
            dates[node] = date

            line = f.readline()

    source_nodes = []
    target_nodes = []
    with open("cit-HepTh.txt", 'r') as f:
        line = f.readline()

        while line:
            if line[0] == "#":
                line = f.readline()
                continue

            both_nodes = list(map(lambda x: int(x.strip()), line.split("\t")))
            source_nodes.append(nodes[0])
            target_nodes.append(nodes[1])

            line = f.readline()

    for i in range(10):
        print(get_metadata(nodes[i]))
