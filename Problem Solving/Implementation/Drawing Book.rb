def solve(n, p)
    # Complete this function
    counter =0
    counterB = 0
    counterA = 0
    pPosition = p%2
    nPosition = n%2
    while n >= p do
        if nPosition === 0
            if n === p
                break
            end
            if n+1 ===p
                break
            end
        end
        if nPosition != 0
            if n === p
                break
            end
            if n-1 ===p
                break
            end
        end
        counterB +=1
        n -=2
    end
    i =1
    while i < p do
        i += 2
        counterA += 1
        if i-1 === p
            break
        end
    end
    if counterA < counterB
        counter = counterA
    else
        counter = counterB
    end
    return counter
    
end