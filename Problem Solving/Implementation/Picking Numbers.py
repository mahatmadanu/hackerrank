def pickingNumbers(a):
    # Complete this function
    resultNumber = []
    sizeNumber = len(a)
    aList = list(sorted(set(a)))
    sizeList = len(aList)
    count = 0
    i = 0
    while i < sizeList :
        j = i + 1
        while j < sizeList:
            temp = aList[i]-aList[j]
            temp = abs(temp)
            if temp==1:
                k = 0
                tempCount = 0
                while k < sizeNumber:
                    if ((a[k]==aList[i]) or (a[k]==aList[j])):
                        tempCount += 1
                    k += 1
                if tempCount > count:
                    count = tempCount
            break;
            j+=1
        l = 0
        tempCount = 0
        while l < sizeNumber:
            if a[l] == aList[i]:
                tempCount+=1
            l +=1
        if tempCount > count:
            count = tempCount
        i += 1
    return count