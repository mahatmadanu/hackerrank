def climbingLeaderboard(scores, alice):
    # Complete this function'
    rank = []
    sizeScores = len(scores)
    sizeScoresAlice = len(alice)
    i = 0
    aliceIndexRank = []
    aliceRank = []
    while i < sizeScores:
        if len(rank)!= 0:
            if scores[i] == scores[i-1]:
                valueRankBefore = rank[i-1]
                rank.append(valueRankBefore)
            else:
                valueRankBefore = rank[i-1]
                value= valueRankBefore + 1
                rank.append(value)
        else:
            rank.append(i)
        i+=1
    i=0
    j = sizeScores-1
    while i < sizeScoresAlice:
        while j >=0 :
            if scores[j] < alice[i]:
                if j == 0 :
                    aliceIndexRank.append(j)
                j = j -1
                if j < 0:
                    j = 0
                    break
                continue
            if scores[j] == alice[i]:
                aliceIndexRank.append(j)
                if j < 0:
                    j = 0
                break
            if scores[j] > alice[i]:
                aliceIndexRank.append(j+1)
                if j < 0:
                    j = 0
                break
            j = j - 1
            if j < 0:
                j = 0
        
        i+=1
    # print(aliceIndexRank)
    i = 0
    while i < len(aliceIndexRank):
        if aliceIndexRank[i] == len(rank):
            aliceRank.append(rank[-1]+1+1)
        else:
            aliceRank.append(rank[aliceIndexRank[i]]+1)
        i+=1
    
    return aliceRank