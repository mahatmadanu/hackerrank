def getTotalX(a, b)
    # Complete this function
    i = 1
    countX = 0
    lengthA = a.length
    lengthB = b.length
    while i <= 100 do
        j = 0
        k = 0
        countModA = 0
        countModB = 0
        while j < lengthA do
            modA = i % a [j]
            if modA === 0
                countModA += 1
            end
        j += 1
        end
        while k < lengthB do
            modB = b[k]%i
            if modB === 0
                countModB += 1
            end
        k += 1
        end
        if countModA === lengthA && countModB === lengthB
            countX += 1
        end
        i+=1
    end
    return countX
end