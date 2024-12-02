import sys
import numpy as np
import pandas as pd

def main(stdin):
    X, Y = [], []
    for row in stdin.split('\n'):
        if row:
            x, y = row.split()
            X.append(int(x))
            Y.append(int(y))

    df = pd.DataFrame.from_dict(dict(
        X = np.array(sorted(X)),
        Y = np.array(sorted(Y))
    ))
    df['DELTA'] = abs(df['Y'] - df['X'])
    
    print(df)
    print("sum(df['DELTA']) =", sum(df['DELTA']))

if __name__ == "__main__":
    main(stdin = sys.stdin.read())
