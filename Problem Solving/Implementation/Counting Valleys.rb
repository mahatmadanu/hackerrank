def countingValleys(n, s)
    # Complete this function
    counter = 0
    counterUp = 0
    counterDown = 0
    counterV = 0
    i = 0
    while i < n do
        if s[i]=== "D"
            counter -= 1
            if counterUp >0
                counterUp -= 1
            end
            counterDown -= 1
        else
            counter += 1
            counterUp += 1
            if counter === 0 && counterDown < 0
                counterV +=1
            end
            if counterDown < 0
                counterDown = counterDown + 1
            end
        end
        
         i += 1
    end
    return counterV
end