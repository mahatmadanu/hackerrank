def hurdleRace(k, height):
    # Complete this function
    magic = 0
    maxHeight = max(height)
    if maxHeight > k:
        magic = maxHeight-k
    return magic