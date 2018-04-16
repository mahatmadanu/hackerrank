def circularArrayRotation(a, m, k, n):
    # Complete this function
    mList = a
    i = 0
    results = []
    if k>n:
        k = k%n
    x = mList[-k:]
    y = x+mList[0:-k]
    mList = y
    for j in m:
        if j >= len(mList):
            continue
        result = mList[j]
        results.append(result)
    return results