import numpy as np

class gradient_descent:
        

    def gradient_descent_regularized(x, y, a = 0.01, t = 15000, l=0.7):
        w = np.zeros((x.shape[1],1))
        b = 0
        
        m = x.shape[0]
        
        for i in range(e):
            h = x @ w + b 
            error = h - y 
            dw = (1/m)* (x.T @ error)
            db = (1/m)* (np.sum(error))
            
            w = w - a*dw - l*w/m 
            b = b - a*db - l*b/m 
            
        return w,b

    #gradient_descent with momentum and regularization. 
    def gradient_descent_momentum(x, y, a = 0.01, t = 10000, l = 0.7, beta = 0.9):

        w = np.zeros((x.shape[1],1))
        b = 0
        
        m = x.shape[0]
        v_w = 0 
        v_b = 0 
        
        for i in range(t):
            h = x @ w + b 
            error = h - y 
            dw = (1/m)* (x.T @ error)
            db = (1/m)* (np.sum(error))
            
            v_w = beta*v_w + (1-beta)*dw 
            v_b = b*v_b + (1-beta)*db 
            
            w = w - a*v_w - l*w/m
            b = b - a*v_b - l*b/m 
            
        return w,b

        #gradient descent with adam optimization. 
    def gradient_descent_adam(x, y, a = 0.1, t = 1500, l = 0.7, beta1 = 0.9, beta2 = 0.999, epsilon = 1e-08):

        w = np.zeros((x.shape[1],1))
        b = 0
        
        m = x.shape[0]
        v_w = 0 
        v_b = 0 
        
        s_w = 0 
        s_b = 0 
        
        for i in range(t):
            h = x @ w + b 
            error = h - y 
            dw = (1/m)* (x.T @ error)
            db = (1/m)* (np.sum(error))
            
            v_w = beta1*v_w + (1-beta1)*dw 
            v_b = beta1*v_b + (1-beta1)*db 
            
            s_w = beta2*s_w + (1-beta2)*dw**2 
            s_b = beta2*s_b + (1-beta2)*db**2 
            
            v_w_c = v_w/(1 - beta1**t)
            v_b_c = v_b/(1 - beta1**t)
            
            s_w_c = s_w/(1 - beta2**t)
            s_b_c = s_b/(1 - beta2**t)
            
            
            
            
            w = w - a*v_w_c/(s_w_c**(0.5) + epsilon) - l*w/m
            b = b - a*v_b_c/(s_b_c**(0.5) + epsilon) - l*b/m 
            
        return w,b

    
        
