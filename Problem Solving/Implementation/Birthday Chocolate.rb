def solve(n, s, d, m)
    # Complete this function
    i = 0
    numberChoc = 0
    while i < n do 
        j = i.dup
        limit = j+m
        if limit > n
            limit = n
        end
        sumChoc = 0
        while j < limit do
            sumChoc += s[j]
            j+=1
        end
        if sumChoc === d
            numberChoc += 1
        end
        i +=1
    end
    return numberChoc
end