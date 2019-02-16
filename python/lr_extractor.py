# Imports
import sys
import math
from statistics import mean
from sklearn.linear_model import LinearRegression


# ------------------------------------------------
# Linear Regression (LR) Extractor
# ------------------------------------------------
class LR_Extractor:
    
    ''' Linear Regression (LR) Extractor '''
    def __init__(self):
        self._model = LeastSquares()
    
    
    '''
    function: 
        - compute(X, Y): feature extraction
    input:
        - X: X-axis values
        - Y: Y-axis values
    return:
        - model: LeastSquares
        - R2: coefficient of determination
        - angle: angle in degrees
    '''
    def compute(self, X, Y):
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
    
    
    '''
    function: (private)
        - _clean(X, Y): remove Nones
    input:
        - X: X-axis values
        - Y: Y-axis values
    return:
        - X: cleaned X-axis values
        - Y: cleaned Y-axis values
    '''
    def _clean(self, X, Y):
        x, y = [], []
        for i in range(len(Y)):
            if(Y[i] is not None):
                x.append(X[i])
                y.append(Y[i])
        return x, y


# ------------------------------------------------
# Simple Linear Regression Model
# ------------------------------------------------
class LeastSquares:

    ''' Simple Linear Regression Model '''
    def __init__(self):
        self._model = None
    
    
    '''
    function: 
        - compute(X, Y): least squares
    input:
        - X: X-axis values
        - Y: Y-axis values
    return:
        - None
    '''
    def compute(self, X, Y):
        alpha, beta = 0, 0
        ran = range(len(X))
        beta = sum([X[i]*Y[i] for i in ran]) - 1/len(X)*sum(X)*sum(Y)
        beta = beta / (sum([X[i]*X[i] for i in ran]) - 1/len(X)*(sum(X)**2))
        alpha = mean(Y) - beta*mean(X)
        self._model = (alpha, beta)
    
    
    '''
    function: 
        - predict(x): prediction
    input:
        - x: x value
    return:
        - y: predicted y value
    '''
    def predict(self, x):
        alpha, beta = self._model
        pred = alpha + beta*x
        return pred
    
    
    '''
    function: 
        - get_model(): get model
    return:
        - model: (alpha, beta)
    '''
    def get_model(self):
        alpha, beta = self._model
        return (alpha, beta)