def extraLongFactorials(n):
    # Complete this function
    result = 1
    while n > 0:
        result = result * n
        # print(result)
        n = n-1
    # return result
    print (result)