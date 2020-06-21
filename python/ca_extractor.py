# Imports
import math

'''
@module: CA_Extractor
Coefficient of Angle (CA) Extractor

@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/paper-2019-iceis GitHub
@license: Apache 2.0 License
@copyright: 2019 Leonardo Mauro
@access: public
'''

class CA_Extractor:
    '''
    Coefficient of Angle (CA) Extractor
    '''

    def __init__(self):
        '''
        Coefficient of Angle object construtor
        '''
        self._T = None


    @classmethod
    def compute(self, X, Y):
        ''' 
        Feature extraction
        @param X: X-axis values
        @param Y: Y-axis values
        @return: T: theta values
        @access: public
        '''
        idx, last = 0, len(Y)-1
        self._T = []
        while idx < last:
            # exist keys? (in range)
            nxt = idx + 1
            if Y[nxt] is not None and Y[idx] is not None:
                delta = Y[nxt] - Y[idx]
                radians = math.atan2(delta, 1)
                degrees = math.degrees(radians)
                self._T.append(degrees)
            idx += 1
        return self._T
