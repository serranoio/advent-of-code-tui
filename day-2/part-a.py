import sys
import numpy as np
import pandas as pd
from collections import defaultdict

def divie_conquer(row):
    n = len(row) 

    if not row:
        return 1
    
    if n == 2:
        delta = abs(int(row[1]) - int(row[0]))
        if delta >= 3:
            return 0
        return 1

    if n == 3:
        running_delta = 0
        for i in range(2):
            delta = int(row[i + 1]) - int(row[i])  
            if delta >= 3:
                return 0
            running_delta += delta / abs(delta) if delta != 0 else 0
            print(delta, running_delta)
        return int(running_delta != 0)

    if divie_conquer(row[:n//2]):
        return divie_conquer(row[n//2 + 1:])
    
    return 0


def main(stdin):
    print(
        "sum(valid_rows) =",
        sum([divie_conquer(row.split()) for row in stdin.split('\n')])
    )
        

if __name__ == "__main__":
    main(stdin = sys.stdin.read())
