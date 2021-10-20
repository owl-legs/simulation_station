# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:47:54 2021

@author: aaaro
"""

import stats

class PopulationMeanEstimator():
    
    def __init__(self, data):
        
        self.data = data
        
        if len(data) < 30:
            
            return('Use Class Object with T-Distribution')
        
    def mean(self):
        
        data = self.data
        
        x_bar = sum(data) / len(data)
        
        return(x_bar)
    
    def variance(self):
        
        data = self.data
        
        mean = self.mean()
        
        n = len(data)
        
        variance = sum([(x - mean)**2 for x in data]) / n - 1
        
        return(variance)
    
    def zcritical(self, alpha):
        
        return(stats.norm.ppf(1 - alpha))
        
    def confidence_interval(self, ci):
        
        alpha = 1 - ci
        
        z_star = self.zcritical(alpha/2)
        
        x_bar = self.mean()
        
        n = len(self.data)
        
        sigmasq = self.variance()
        
        return(x_bar - z_star*((sigmasq / n)**1/2), \
                x_bar + z_star*((sigmasq / n)**1/2))
    
    def margin_of_error(self, ci):
        
        lower, upper = self.confidence_interval(ci)
        
        x_bar = self.mean()
        
        return(upper - x_bar)
    
    def minimum_sample_size(self, ci, error_bound):
        
        alpha = 1 - ci
        
        z_star = self.zcritical(alpha / 2)
        
        sigmasq = self.variance()
        
        minimum = ((z_star * (sigmasq**1/2))/error_bound)**2
        
        return(int(minimum))
        
    
        
        
