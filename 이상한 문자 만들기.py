def solution(s):
    answer = ""
    for word in s.split(" "):
        for idx in range(len(word)):
            if idx % 2 == 0:
                answer+=word[idx].upper()
            else:
                answer+=word[idx].lower()
        answer+=" "
    
    return answer[:-1]
  
# 다른풀이
def solution(s):
    return " ".join(map(lambda x: "".join(c.upper() if idx % 2 ==0 else c.lower() for idx, c in enumerate(x)), s.split(" ")))
