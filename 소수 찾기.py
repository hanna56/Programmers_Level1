def solution(n):
    lst = [True] * (n+1)
    for i in range(2, int(n**(1/2))+1):
        if lst[i]:
            for j in range(2*i, n+1, i):
                lst[j] = False
    
    return lst[2:].count(True)
