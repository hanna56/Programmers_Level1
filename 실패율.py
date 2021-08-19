def solution(N, stages):
    answer_dict = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if total == 0:
            answer_dict[i] = 0
        else:
            answer_dict[i] = stages.count(i) / total
            total -= stages.count(i)
        
    return [j[0] for j in sorted(answer_dict.items(), key = lambda x: x[1], reverse=True)]
    # 더 좋은 return 코드
    #return sorted(answer_dict, key = answer_dict.get, reverse = True)
    #return sorted(answer_dict, key = lambda x: answer_dict[x], reverse = True)
    #return sorted(answer_dict.keys(), key = lambda x: answer_dict[x], reverse = True)
