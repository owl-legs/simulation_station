import random
import numpy as np

def monte_carlo(data, nsim, with_replacement, func):
    if with_replacement == 1:
        samps = [func(random.choices(data, k=len(data))) for i in range(0, nsim)]
    else:
        samps = [func(random.sample(data, k=len(data))) for i in range(0, nsim)]
    return(np.mean(samps))
   
