def viralAdvertising(n):
    # Complete this function
    receivedShare = 5
    likedShare = 0
    i = 1
    while i <= n:
        dislikedShare = receivedShare-(int(receivedShare/2))
        likedShare += receivedShare-dislikedShare
        receivedShare = (int(receivedShare/2)) * 3
        i += 1
    return likedShare