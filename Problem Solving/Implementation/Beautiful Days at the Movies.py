def beautifulDays(i, j, k):
    # Complete this function
    number = []
    reversedNumber = []
    beautiful = 0
    while i <= j:
        strNumber = str(i)
        tempReversedStrNumber = ""
        for c in reversed(strNumber):
            tempReversedStrNumber = tempReversedStrNumber+c
        tempReversedIntNumber = int(tempReversedStrNumber)
        number.append(i)
        reversedNumber.append(tempReversedIntNumber)
        i += 1
    l = 0
    while l < len(number):
        mod = number[l]-reversedNumber[l]
        if mod % k == 0:
            beautiful+= 1
        l += 1
    return beautiful