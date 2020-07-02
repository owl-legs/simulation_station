#batch means program for time series
#returns pandas df with:
    #Expected Slope
    #Variance of Expected Slope
    #95% confidence interval
import numpy as np
import pandas as pd

def split_data(data, K, N):
    return(np.array_split(data[int(K):], N))

def sample_var(batch):
    x_bar = np.mean(batch)
    return((sum(np.power(abs(batch - x_bar), 2))/(len(batch)-1.0)))

def slope(batch):
    batch = list(batch['4'])
    dy = float(batch[len(batch) -1]) - float(batch[0])
    dx = float(len(batch))
    return(dy/dx)

def ci_95(mu, var, N):
    return[mu - (1.96*(np.sqrt(var)/np.sqrt(N))),
           mu + (1.96*(np.sqrt(var)/np.sqrt(N)))]

def batch_means(data, K, N):
    batches = split_data(data, K, N)
    av_slope = [slope(batch) for batch in batches]

    batch_averages = []
    batch_var = []
    output_summaries = []

    mu = np.mean(av_slope)
    svar = sample_var(av_slope)
    conf = ci_95(mu, svar, N)
        
    row = [mu, svar, str('[') +str(np.round(conf[0], 5)) + ", " + str(np.round(conf[1], 5)) + str(']')]
    output_summaries.append(row)
    
    output_summaries = pd.DataFrame(output_summaries)
    output_summaries['Metric'] = ['Average Slope']
    output_summaries = output_summaries[['Metric', 0, 1, 2]]
    output_summaries = output_summaries.rename(columns={0:'E(x)', 
                                                        1:'var(x)', 
                                                        2:'95% Confidence Interval'})
    
    return(output_summaries)

