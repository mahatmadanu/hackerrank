def cutTheSticks(arr):
    # Complete this function
    sortedArr = sorted(arr)
    result = []
    i = 0
    while i < len(sortedArr):
        resultArr = cut(sortedArr)
        result.append(resultArr[1])
        sizeResultArr = len(resultArr[0])
        if sizeResultArr==0:
            break
        else:
            sortedResultArr = sorted(resultArr[0])
            sortedArr = sortedResultArr
            i +=0
    return result

def cut(newArr):
    result = []
    counter = 0
    cutter = newArr[0]
    i = 0
    while i < len(newArr):
        if newArr[i]< cutter:
            i += 1
            continue
        else:
            temp = newArr[i]-cutter
            if temp != 0:
                result.append(temp)
            counter += 1
        i+=1
    return [result,counter]