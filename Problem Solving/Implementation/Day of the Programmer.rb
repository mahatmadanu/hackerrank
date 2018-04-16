def solve(year)
    # Complete this function
    daysInMonth = [nil, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    if year < 1918
        if year % 4 === 0
            daysInMonth[2] = 29
        end
    else
       if ((year%4 ===0 && year%100 != 0) || (year % 400 === 0))
        daysInMonth[2] = 29
       end
        if year === 1918
            daysInMonth[2] = daysInMonth[2]-13 
        end
    end
    flag = 0
    i = 1
    sum = 0
    date = "0"
    month = "0"
    while i < daysInMonth.length do
        sum += daysInMonth[i]
        if sum > 256 
            flag = i-1
            break
        end
        i+=1 
    end
    result = sum-daysInMonth[i]
    
    result = 256-result
    if result < 10
        result = result.to_s
        date << result
    else
        date = result.to_s
    end
    if i < 10
        i = i.to_s
        month << i
    else
        month = i.to_s
    end
    date = date << "."
    month = month << "."
    date << month
    date << year.to_s
    return date
end