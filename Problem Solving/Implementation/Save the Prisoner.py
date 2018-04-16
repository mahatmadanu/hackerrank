def saveThePrisoner(n, m, s):
    # Complete this function
    candies = m % n
    # print (candies)
    result = 0
    receivedCandy = candies-1
    if candies !=0 :
        tempResult = s+receivedCandy
        if tempResult > n:
            tempResult = tempResult-n
            result = tempResult
        else:
            result = tempResult
    else:
        tempResult = s - 1
        if tempResult == 0:
            result = n
        else:
            result = tempResult
        
    return result