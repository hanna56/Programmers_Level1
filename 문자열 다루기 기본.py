def solution(s):
    if (len(s) == 4 or len(s) == 6):
        try:
            int(s)
            return True
        except:
            return False
    else:
        return False
    
    
    
# 다른풀이
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
