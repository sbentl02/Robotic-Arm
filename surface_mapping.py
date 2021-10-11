import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import adafruit_vl53l0x
import board
import busio

def fit_func(data, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16):
    x = data[0]
    y = data[1]
    return c1 + c2 * y + c3*y**2 + c4*y**3 + c5*x + c6*x*y + c7*x*y**2 + c8*x*y**3 + c9*x**2 + c10*x**2*y + c11*x**2*y**2 + c12*x**2*y**3 + c13*x**3 + c14*x**3*y + c15*x**3*y**2 + c16*x**3*y**3

def surface_approximation(n_samples, Z_data, xmin=-100, xmax=100, ymin=-100, ymax=100):

    x = np.linspace(xmin, xmax, n_samples).reshape(n_samples, 1)
    y = np.linspace(ymin, ymax, n_samples).reshape(1, n_samples)
    
    features = {}
    features['x^0*y^0'] = np.matmul(x**0, y**0).flatten()
    features['x^0*y'] = np.matmul(x**0, y).flatten()
    features['x^0*y^2'] = np.matmul(x**0, y**2).flatten()
    features['x^0*y^3'] = np.matmul(x**0, y**3).flatten()
    features['x*y^0'] = np.matmul(x, y**0).flatten()
    features['x*y'] = np.matmul(x, y).flatten()
    features['x*y^2'] = np.matmul(x, y**2).flatten()
    features['x*y^3'] = np.matmul(x, y**3).flatten()
    features['x^2*y^0'] = np.matmul(x**2, y**0).flatten()
    features['x^2*y'] = np.matmul(x**2, y).flatten()
    features['x^2*y^2'] = np.matmul(x**2, y**2).flatten()
    features['x^2*y^3'] = np.matmul(x**2, y**3).flatten()
    features['x^3*y^0'] = np.matmul(x**3, y**0).flatten()
    features['x^3*y'] = np.matmul(x**3, y).flatten()
    features['x^3*y^2'] = np.matmul(x**3, y**2).flatten()
    features['x^3*y^3'] = np.matmul(x**3, y**3).flatten()

    data = pd.DataFrame(features)

    reg = LinearRegression().fit(data.values, Z_data.flatten())

    return reg.intercept_, reg.coef_
    

def sample_surface(n_samples, xbounds, ybounds):
    #Move motor to sample location, take data, record to numpy array
    np.empty((n_samples, n_samples))
    return



