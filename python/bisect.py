def bisection(f,a,b,epsilon = 1e-7,maxiter = 1000): 
    if f(a)*f(b)> 0: 
        print('wrong choice bro')
    else: 
        p = (a + b)/2.0 
        err = abs(f(p))
        count = 0
        while count < maxiter and err > epsilon: 
            if f(a)*f(p)< 0: 
                b = p
            else: 
                a = p 
            p = (a + b)/2.0
            err = abs(f(p))
            count += 1
        return p    
