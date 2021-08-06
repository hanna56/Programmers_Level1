def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i % 2 == 0:
            answer+="박"
        else:
            answer+="수"
    return answer
  
  
  # 다른 풀이
  def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
