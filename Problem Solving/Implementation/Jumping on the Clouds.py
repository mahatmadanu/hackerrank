def jumpingOnClouds(c):
    # Complete this function
    sizeC = len(c)
    counter = 0
    i = 0
    while i <sizeC:
        checkNext2 = i+2
        checkNext1 = i+1
        if checkNext2 >= sizeC and checkNext1>=sizeC:
            break
        elif checkNext2 >=sizeC and checkNext1 < sizeC:
            counter +=1
            i+=1
        else:
            if c[checkNext2] == 1:
                counter+=1
                i+=1
            else:
                counter +=1
                i+=2
    return counter