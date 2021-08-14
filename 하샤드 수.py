def solution(x):
    sum_x = 0
    for i in str(x):
        sum_x+=int(i)        
    return x % sum_x == 0

  
# 다른풀이
def solution(x):
    return x % sum([int(num) for num in str(x)]) == 0
