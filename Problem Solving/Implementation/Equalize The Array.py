def equalizeArray(arr):
    # Complete this function
    i = 0
    countedValue = 0
    rMax = 0
    sizeArr = len(arr)
    result = 0
    while i < sizeArr:
        temp = arr[i]
        if countedValue==temp:
            i+=1
            continue
        else:
            tempMax = arr.count(temp)
            if tempMax > rMax:
                rMax=tempMax
        i +=1
    result = sizeArr-rMax
    return result