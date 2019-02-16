# Imports
import sys
import math
import scipy as sc
import pandas as pd


# ------------------------------------------------
# Delta Rank (DR) Extractor
# ------------------------------------------------
class DR_Extractor:
    
    ''' Delta Rank (DR) Extractor '''
    def __init__(self):
        self._D = None


    '''
    function: 
        - compute(X, Y): feature extraction
    input:
        - X: X-axis values
        - Y: Y-axis values
    return:
        - D: delta values
        - S(D): entropy of D
    '''
    def compute(self, X, Y):
        idx, last = 0, len(Y)-1
        self._D = []
        while idx < last:
            # exist keys? (in range)
            nxt = idx + 1
            if Y[nxt] is not None and Y[idx] is not None in Y:
                delta = Y[nxt] - Y[idx]
                self._D.append(delta)
            idx += 1
        return self._D, self._entropy(self._D)

    
    '''
    function: (private)
        - _entropy(values): compute the entropy
    input:
        - values: number values
    return:
        - S: entropy
    '''
    def _entropy(self, values):
        serie = pd.Series(values)
        p_data = serie.value_counts() / len(serie)  # calculates the probabilities
        score = sc.stats.entropy(p_data)  # input probabilities to get the entropy
        return score