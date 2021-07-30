def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]





# 다른 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
