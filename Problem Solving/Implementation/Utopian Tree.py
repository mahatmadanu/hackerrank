def utopianTree(n):
    # Complete this function
    tree = 1
    j = n
    weather = "spring"
    while j >= 1:
        if weather == "spring":
            tree = tree * 2
            weather = "summer"
        else :
            tree = tree + 1
            weather = "spring"
        j = j - 1
    return tree