# Imports
import sys
import math
import scipy as sc
import pandas as pd


# ------------------------------------------------
# Delta Rank (DR) Extractor
# ------------------------------------------------
class DR_Extractor:

    # Init the model
    def __init__(self):
        self._D = None

    # Extraction
    #- X: X-axis values
    #- Y: Y-axis values
    #- return: D, entropy(D)
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

    # Entropy
    #- values: list of values
    def _entropy(self, values):
        serie = pd.Series(values)
        p_data = serie.value_counts() / len(serie)  # calculates the probabilities
        score = sc.stats.entropy(p_data)  # input probabilities to get the entropy
        return score