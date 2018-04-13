def repeatedString(s, n):
    # Complete this function
    charPos = []
    sizeS = len(s)
    for i, c in enumerate(s):
        if "a"==c: 
            charPos.append(i+1)
    tempResult = (int(n/sizeS))*len(charPos)
    modResult = n%sizeS
    if modResult != 0:
        i = 0
        while i < len(charPos):
            if charPos[i] <= modResult:
                tempResult += 1
            else:
                break
            i += 1

    return tempResult