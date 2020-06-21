# Imports
import scipy as sc
import pandas as pd

'''
@module: DR_Extractor
Delta Rank (DR) Extractor

@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/paper-2019-iceis GitHub
@license: Apache 2.0 License
@copyright: 2019 Leonardo Mauro
@access: public
'''

class DR_Extractor:
    '''
    Delta Rank (DR) Extractor
    '''

    def __init__(self):
        '''
        Delta Rank object construtor
        '''
        self._D = None


    @classmethod
    def compute(self, X, Y):
        ''' 
        Feature extraction
        @param X: X-axis values
        @param Y: Y-axis values
        @return: D: delta values, S(D): entropy of D
        @access: public
        '''
        idx, last = 0, len(Y)-1
        self._D = []
        while idx < last:
            # exist keys? (in range)
            nxt = idx + 1
            if Y[nxt] is not None and Y[idx] is not None:
                delta = Y[nxt] - Y[idx]
                self._D.append(delta)
            idx += 1
        return self._D, self._entropy(self._D)

    
    @classmethod
    def _entropy(self, values):
        ''' 
        Compute the entropy
        @param values: array of values
        @return: S: entropy of a set
        @access: private
        '''
        serie = pd.Series(values)
        p_data = serie.value_counts() / len(serie)  # calculates the probabilities
        score = sc.stats.entropy(p_data)  # input probabilities to get the entropy
        return score
