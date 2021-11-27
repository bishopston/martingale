import numpy as np
from scipy.stats import norm

def delta(option_type, sigma, So, K, r, T):
    sigma = float(sigma)
    d1 = (np.log(So / K) + (r + sigma ** 2 * 0.5) * T) / (sigma * np.sqrt(T))
    if option_type == 'c':
        value = norm.cdf(d1)
        return value
    elif option_type == 'p':
        value = norm.cdf(d1) - 1
        return value
    else:
        print('No such option type %s') %option_type

def _n(x):
    return np.exp(-x ** 2 / 2) / np.sqrt(2 * 3.14)

def theta(option_type, sigma, So, K, r, T):
    sigma = float(sigma)
    d1 = (np.log(So / K) + (r + sigma ** 2 * 0.5) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'c':
        value = (-((So * _n(d1) * sigma)/ (2 * np.sqrt(T)))-(r * K * np.exp(-r * T) * norm.cdf(d2)))/252
        return value
    elif option_type == 'p':
        value = (-((So * _n(d1) * sigma)/ (2 * np.sqrt(T)))+(r * K * np.exp(-r * T) * norm.cdf(-d2)))/252
        return value
    else:
        print('No such option type %s') %option_type

def gamma(sigma, So, K, r, T):
    sigma = float(sigma)
    d1 = (np.log(So / K) + (r + sigma ** 2 * 0.5) * T) / (sigma * np.sqrt(T))
    value = (_n(d1) / (So * sigma * np.sqrt(T)))
    if sigma != 0:
        return value
    else:
        return 0.0

def vega(sigma, So, K, r, T):
    sigma = float(sigma)
    d1 = (np.log(So / K) + (r + sigma ** 2 * 0.5) * T) / (sigma * np.sqrt(T))
    value = 0.01 * So * np.sqrt(T) * _n(d1)
    return value