# Imports
import math
from statistics import mean
from sklearn.linear_model import LinearRegression

'''
@module: LR_Extractor
Linear Regression (LR) Extractor

@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/paper-2019-iceis GitHub
@license: Apache 2.0 License
@copyright: 2019 Leonardo Mauro
@access: public
'''

class LR_Extractor:
    '''
    Linear Regression (LR) Extractor
    '''

    def __init__(self):
        '''
        Linear Regression construtor
        '''
        self._model = LeastSquares()
    
    
    @classmethod
    def compute(self, X, Y):
        ''' 
        Feature extraction
        @param X: X-axis values
        @param Y: Y-axis values
        @return: model: LeastSquares, R2: coefficient of determination, angle
        @access: public
        '''
        X, Y = self._clean(X, Y)
        # Least Squares
        reg = LinearRegression().fit([[i] for i in X], Y)
        self._model.compute(X, Y)
        r2 = reg.score([[i] for i in X], Y)
        # Angle in degrees
        x = [X[0], X[len(X)-1]]
        y = list(map(lambda a: reg.predict([[a]])[0], x))
        radians = math.atan2(y[1]-y[0], x[1]-x[0])
        degrees = math.degrees(radians)
        # return
        return self._model, r2, degrees
    
    
    @classmethod
    def _clean(self, X, Y):
        ''' 
        Clean the None values
        @param X: X-axis values
        @param Y: Y-axis values
        @return: new X, Y-axis
        @access: private
        '''
        x, y = [], []
        for i, value in enumerate(Y):
            if(value is not None):
                x.append(X[i])
                y.append(value)
        return x, y

'''
@module: LeastSquares
Simple Linear Regression Model

@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/paper-2019-iceis GitHub
@license: Apache 2.0 License 
@copyright: 2019 Leonardo Mauro
@access: public
'''

class LeastSquares:
    '''
    Simple Linear Regression Model
    '''

    def __init__(self):
        '''
        Linear Regression object construtor
        '''
        self._model = None
    
    
    @classmethod
    def compute(self, X, Y):
        ''' 
        Compute least squares
        @param X: X-axis values
        @param Y: Y-axis values
        @return: None
        @access: public
        '''
        alpha, beta = 0, 0
        ran = range(len(X))
        beta = sum([X[i]*Y[i] for i in ran]) - 1/len(X)*sum(X)*sum(Y)
        beta = beta / (sum([X[i]*X[i] for i in ran]) - 1/len(X)*(sum(X)**2))
        alpha = mean(Y) - beta*mean(X)
        self._model = (alpha, beta)
    
    
    @classmethod
    def predict(self, x):
        ''' 
        Prediction
        @param x: x value
        @return: y: predicted y value
        @access: public
        '''
        alpha, beta = self._model
        pred = alpha + beta*x
        return pred
    
    
    @classmethod
    def get_model(self):
        ''' 
        Get model (alpha, beta)
        @return: model
        @access: public
        '''
        alpha, beta = self._model
        return (alpha, beta)
