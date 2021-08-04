from itertools import combinations

def solution(nums):
    answer = 0
    count = 0
    for comb in combinations(nums,3):
        for i in range(1, sum(comb)+1):   
            if sum(comb) % i == 0 :
                count += 1
        if count == 2:
            answer += 1
        count = 0

    return answer
