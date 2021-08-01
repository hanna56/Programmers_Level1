def solution(a, b):
    answer = 0
    for idx, k in enumerate(a):
        answer += k * b[idx]
    return answer
  
  
  
# 다른 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
