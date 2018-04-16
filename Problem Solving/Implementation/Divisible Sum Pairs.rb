def divisibleSumPairs(n, k, ar)
    # Complete this function
    i = 0 
    count = 0
    while i < n do 
        j = i + 1
        while j < n do
            temp = 0
            temp = ar[i]+ar[j]
            if temp % k === 0
                count +=1
            end
            j += 1
        end
        i += 1
    end
    return count
end