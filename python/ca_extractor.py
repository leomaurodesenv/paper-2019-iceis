# Imports
import sys
import math


# ------------------------------------------------
# Coefficient of Angle (CA) Extractor
# ------------------------------------------------
class CA_Extractor:

    # Init the model
    def __init__(self):
        self._T = None

    # Extraction
    #- X: X-axis values
    #- Y: Y-axis values
    #- return: T
    def compute(self, X, Y):
        idx, last = 0, len(Y)-1
        self._T = []
        while idx < last:
            # exist keys? (in range)
            nxt = idx + 1
            if Y[nxt] is not None and Y[idx] is not None in Y:
                delta = Y[nxt] - Y[idx]
                radians = math.atan2(delta, 1)
                degrees = math.degrees(radians)
                self._T.append(degrees)
            idx += 1
        return self._T