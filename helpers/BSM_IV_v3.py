import numpy as np
from scipy.stats import norm

def bsm_price(option_type, sigma, So, K, r, T):
    # calculate the bsm price of European call and put options
    sigma = float(sigma)
    d1 = (np.log(So / K) + (r + sigma ** 2 * 0.5) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'c':
        price = So * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
        return price
    elif option_type == 'p':
        price = np.exp(-r*T) * K * norm.cdf(-d2) - So * norm.cdf(-d1)
        return price
    else:
        print('No such option type %s') %option_type
		
		
def implied_vol(option_type, option_price, So, K, r, T):
	precision = 0.00001
	iterations = 0
	max_vol = 500.0
	min_vol = 0.0001
	mid_vol = (max_vol + min_vol)*0.5
	
	while 1:
		iterations +=1
		
		if option_type == 'c':
		
			mid_vol = (max_vol + min_vol)*0.5
			price= bsm_price(option_type, mid_vol, So, K, r, T)
			
			if price - option_price > precision:
				max_vol = mid_vol
			else:
				min_vol = mid_vol
				
			if abs(price - option_price) < precision: break
			if iterations > 100: break
	
		elif option_type == 'p':
		
			mid_vol = (max_vol + min_vol)*0.5
			price= bsm_price(option_type, mid_vol, So, K, r, T)
			
			if option_price - price > precision:
				min_vol = mid_vol
			else:
				max_vol = mid_vol
				
		if abs(price - option_price) < precision: break
		if iterations > 100: break
	
	#print(K, mid_vol)
	return mid_vol
	
