import sys
import numpy as np
import pandas as pd
from collections import defaultdict

def main(stdin):
    X, Y = [], []
    for row in stdin.split('\n'):
        if row:
            x, y = row.split()
            X.append(int(x))
            Y.append(int(y))

    Y_freq = defaultdict(int)
    for num in set(X):
        Y_freq[num] = Y.count(num)

    X_freq = {num: Y_freq[num] for num in X} 

    print(
        'sum([num  * freq for num, freq in X_freq.items()] =', 
        sum([num  * freq for num, freq in X_freq.items()])
    )

if __name__ == "__main__":
    main(stdin = sys.stdin.read())
