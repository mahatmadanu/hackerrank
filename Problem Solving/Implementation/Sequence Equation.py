def permutationEquation(p):
    p = [0]+p
    i = 1
    result = []
    while i < len(p):
        
        index = p.index(i)
        index = p.index(index)
        result.append(index)
        i+=1
    return result