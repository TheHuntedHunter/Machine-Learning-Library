import numpy as np 
class data_preprocessing:

    def normalize(x):
        min_val = np.min(x, axis=0)
        max_val = np.max(x, axis=0)
        ranges = max_val - min_val 
        
        ranges[ranges == 0] = 1 
       
        normalized_data = (x - min_val) / ranges
        return normalized_data

    def standardize(x):
        x_mean = np.mean(x, axis=0)
        x_std = np.std(x, axis=0)
        
        standardized_data = (x - x_mean) / x_std
        return standardized_data

