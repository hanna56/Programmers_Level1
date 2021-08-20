def solution(strings, n):
    dic = {}
    for s in strings:
        dic[s]=s[n]
    return sorted(sorted(dic), key = dic.get)
  
# 다른풀이
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x: x[n])
        
