def breakingRecords(score)
    # Complete this function
    i = 0
    recordScore = 0
    recordCount = 0
    worstScore = 0
    worstCount = 0
    while i < score.length do
        if i === 0 
            recordScore = score[i]
            worstScore = score[i]
        end
        if i > 0
            if score[i] < worstScore
                worstCount +=1 
                worstScore = score[i]
            end
            if score[i] > recordScore
                recordCount +=1
                recordScore = score[i]
            end
        end
        i += 1
    end
    return [recordCount, worstCount]
end