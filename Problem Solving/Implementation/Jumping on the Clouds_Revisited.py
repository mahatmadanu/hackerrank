def jumpingOnClouds(c, k):
    # Complete this function
    e = 100
    i = 0
    while i < len(c):
        
        if c[i]==0:
            e = e-1
        if c[i]==1:
            e = e-2-1
        i += k 
    return e