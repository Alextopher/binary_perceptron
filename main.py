import numpy as np

pairs = []
with open('train-a1-449.txt') as f:
    for line in f.readlines():
        split = line.split(' ')
        nums = np.array([float(n) for n in split[:1024]])
        is_yes = split[-1] == 'Y'
        pairs.append((nums, is_yes))
