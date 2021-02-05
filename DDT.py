import pandas as pd
import numpy as np

sbox = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14] 

def print_differential_prob_table(sbox):
    dim = len(sbox)
    np.set_printoptions(formatter={'int': hex})
    prob = np.zeros(shape=(dim, dim))

    for i in range(dim):
        for j in range(dim):
            prob[i ^ j, sbox[i] ^ sbox[j]] += 1

    cols = []
    rows = []

    for i in range(dim):
        cols.append(str(i))
        rows.append(str(i))

    print("SBox: ", sbox)
    print()

    df = pd.DataFrame(prob, index = rows, columns = cols, dtype=int)
    print("DDT")
    print(df)
    print()


print_differential_prob_table(sbox)