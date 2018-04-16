def angryProfessor(k, a):
    # Complete this function
    sizeOfA = len(a)
    i = 0
    inClass = 0
    cancelOrNo = "YES"
    while i < sizeOfA:
        if a[i] <= 0:
            inClass += 1
        i += 1
    if inClass >= k:
        cancelOrNo = "NO"
        
    return cancelOrNo