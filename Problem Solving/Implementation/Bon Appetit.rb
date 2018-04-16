def bonAppetit(n, k, b, ar)
    # Complete this function
    i = 0
    total = 0
    tempAnna =0
    tempBrian = ar[k]
    shareCostTotal = 0
    shareCost = 0
    shareCostActual = 0
    result = ""
    while i < n do
        total += ar[i]
        i += 1
    end 
    shareCostTotal = total/2
    shareCostActual = total - tempBrian
    shareCostActual = shareCostActual/2
  
    tempAnna = shareCostTotal - shareCostActual
    if shareCostActual === b
        result = "Bon Appetit"
    else
         result = tempAnna.to_s
    end
   
    return result
end