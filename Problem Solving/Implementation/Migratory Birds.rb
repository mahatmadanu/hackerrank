def migratoryBirds(n, ar)
    # Complete this function
    i = 1 
    typeOfBirds = [[],[],[],[],[],[]]
    countBirds = 0
    commonBird = 0
    while i < n do
        if ar[i]>5
            continue
        end
        typeOfBirds[ar[i]].push(ar[i])
        i += 1
    end
    typeOfBirds.each_with_index do |flock, xi| 
        if flock.length === 0
            next
        end
        if flock.length > countBirds
            countBirds = flock.length
            commonBird = flock[0]
        end
        if flock.length === countBirds
            if commonBird > flock[0]
                commonBird = flock[0]
            end
        end
    end
    return commonBird
end