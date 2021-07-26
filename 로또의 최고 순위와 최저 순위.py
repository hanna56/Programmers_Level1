# 내 풀이
def rank(score):
    if score <=1:
        rank = 6
    else:
        rank = 7 - score
    return rank

def solution(lottos, win_nums):
    zeros = 0
    wins = 0
    for num in lottos:
        if num==0:
            zeros += 1
            continue
        for win_num in win_nums:
            if num == win_num:
                wins += 1
                
    return rank(wins + zeros), rank(wins)
    
 
 
# 모범 답안
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
