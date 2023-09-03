
path = "../data/"


aligned_type = []
with open("../data/prox_graph/aligned_type.txt", 'r') as f:
    for line in f:
        aligned_type.append(line.strip('\n').split(','))


