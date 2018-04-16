def kangaroo(x1, v1, x2, v2)
    # Complete this function
    i = 1
    kangoroo1 =x1
    kangoroo2 =x2
    while i <= 10000 do
        kangoroo1 += v1
        kangoroo2 += v2
        if kangoroo1 === kangoroo2
            return "YES"
            break
        end
        if i === 10000 && kangoroo1 != kangoroo2
            return "NO"
        end
        i += 1
    end
end