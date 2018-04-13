def camelcase(s):
    # Complete this function
    result = sum(1 for c in s if c.isupper())
    return result+1