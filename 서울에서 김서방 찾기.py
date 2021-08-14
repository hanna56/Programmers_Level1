def solution(seoul):
    for idx in range(len(seoul)):
        if seoul[idx] == "Kim":
            return f"김서방은 {int(idx)}에 있다" 
    
    
    
# 다른 풀이
def solution(seoul):
    return "김서방은 "+ str(seoul.index("Kim"))+"에 있다" 
