def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer
  
# 다른풀이
def solution(n):
    return list(map(int, reversed(str(n))))
