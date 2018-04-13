def findDigits(n, t):
    strN = str(n)
    count = 0
    for c in strN:
        intN = int(c)
        if intN == 0:
            continue
        result = n%intN
        if result == 0:
            count += 1
    # # Complete this function
    return count