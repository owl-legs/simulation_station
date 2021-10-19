# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 22:38:08 2021

@author: aaaro
"""
import random

class ResivoirSampler():
    
    def __init__(self, data, k):
        
        self.data = data
        self.k = k
        
    def sample(self):
        
        data = self.data
        k = self.k
        
        samples = []
        N = 0
        
        for point in data:
            
            N += 1
            
            if len(samples) < k:
                
                samples += [point]
                
            else:
                
                index = random.randint(0, N)
                
                if index < k:
                    samples[index] = point 
                    
        return(samples)
    
    def sample_wiki(self):
        
        n = len(self.data)
        data = self.data
        k = self.k
        
        samples = []
        
        for i in range(k):
            samples.append(data[i])
        
        for i in range(k+1, n):
            
            j = random.randint(0, i-1)
            
            if j < k:
                
                samples[j] = data[i]
        
        return(samples)
    
    

iterable = list(range(1, 1000))

samples = ResivoirSampler(iterable, 100).sample()
print(samples)

samples = ResivoirSampler(iterable, 100).sample_wiki()
print(samples)


                
                
