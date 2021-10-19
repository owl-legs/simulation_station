# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:36:40 2021

@author: aaaro
"""
import random

class InverseTransform():
    
    def __init__(self, pdf, n):
        
        self.pdf = pdf
        self.n = n
        
    def cdf(self):
        
        pdf = self.pdf
        
        cdf = [sum(pdf[:i]) for i in range(1, 1 + len(pdf))]
        
        return(cdf)
    
    def binary_search(self, x, cdf):
        
        pdf = self.pdf
        
        l, r = 0, len(cdf) - 1
        
        while l <= r:
            
            M = (l + r)//2
            
            if x < cdf[M]:
                
                r = M - 1
            
            else:
                
                l = M + 1
        
        index = min(l, r)
    
        return(pdf[index])

    def sample(self):
        
        cdf = self.cdf()
        n = self.n
        
        runif = [random.random() for _ in range(n)]
        samples = [self.binary_search(x, cdf) for x in runif]
        
        return(samples)

#a uniform probability distribution
pdf = [0.1 for i in range(10)]

samples = RejectionSampler(pdf, 1000).sample()

import matplotlib.pyplot as plt

plt.plot(range(len(samples)), samples, marker='o')

