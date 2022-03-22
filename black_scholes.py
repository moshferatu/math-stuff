import numpy as np

from scipy.stats import norm

interest_rate = 0.00
underlying_price = 100
strike_price = 105
time = 30.0 / 365.0
implied_volatility = 0.30

def black_scholes(interest_rate, underlying_price, strike_price, time, implied_volatility, contract_type):
    d1 = (np.log(underlying_price / strike_price) + (interest_rate + implied_volatility**2/2)*time)/(implied_volatility * np.sqrt(time))
    d2 = d1 - (implied_volatility * np.sqrt(time))
    if contract_type == 'C':
        option_price = (underlying_price * norm.cdf(d1, 0, 1)) - (strike_price * np.exp(-interest_rate * time) * norm.cdf(d2, 0, 1))
    else:
        option_price = strike_price * np.exp(-interest_rate * time) * norm.cdf(-d2, 0, 1) - underlying_price*norm.cdf(-d1, 0, 1)
    return option_price

print('Option Price:', round(black_scholes(interest_rate, underlying_price, strike_price, time, implied_volatility, contract_type='C'), 2))