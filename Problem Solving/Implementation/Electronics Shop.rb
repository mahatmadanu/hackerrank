def getMoneySpent(keyboards, drives, s)
    # Complete this function
    is = 0
    sumMoney = s
    iKeyboards = 0
    prices = []
    boughtStuff = -1
    change =0
    result = 0

    while iKeyboards < keyboards.length do
         iDrives = 0
        while iDrives < drives.length do
            sum = keyboards[iKeyboards] + drives[iDrives]
            prices.push(sum)
            iDrives += 1
        end
        iKeyboards += 1
    end
    iPrices = 0
    while iPrices < prices.length do
        if prices[iPrices]===sumMoney
            boughtStuff = prices[iPrices]
            break
        elsif prices[iPrices] < sumMoney
            if change === 0
                change = sumMoney - prices[iPrices]
            else
                tempChange = sumMoney - prices[iPrices]
                if tempChange <= change
                    change = tempChange
                    boughtStuff = prices[iPrices]
                end
            end
        else
            bougthStuff = -1
        end
        iPrices += 1
    end
    # puts boughtStuff
    return boughtStuff
end