def sockMerchant(n, ar)
    # Complete this function
    i =0
    pairs = 0
    while i < n do
        j = i + 1
        while j < n do
            if ar[i] === ar[j]
                pairs+=1
                ar[j]= ar[j] * -1
                break
            end
            j += 1
        end
        i += 1
    end
    return pairs
end