import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import sys

def main(pos, i, d_model):
    # pos: position of token
    # i: dimension of word embedding
    # d_model: dimension of hidden layer

    even_i = np.arange(0, i, 2, dtype='int')
    odd_i = np.arange(1, i, 2, dtype='int')
    pe_1 = []
    pe_2 = []

    for _pos in range(pos):
        pe_even = np.sin(_pos / np.power(10000, (2 * even_i / d_model)))
        pe_odd = np.cos(_pos / np.power(10000, (2 * odd_i / d_model)))
        pe_1.append(np.insert(pe_even, list(range(1, len(pe_odd) + 1)), pe_odd))
        pe_2.append(np.concatenate([pe_even, pe_odd]))

    plt.figure()
    sns.heatmap(pe_1, cmap='GnBu')
    plt.savefig('pe_1.png')
    plt.clf()
    sns.heatmap(pe_2, cmap='GnBu')
    plt.savefig('pe_2.png')
    

if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        print('Check arguments.')

