def solution(s):
    middle = len(s) // 2
    if len(s) % 2 == 1:
        return s[middle]
    else:
        return s[middle-1:middle+1]
 

# 다른풀이
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]
    
