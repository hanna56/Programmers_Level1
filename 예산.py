def solution(d, budget):
    money = 0
    if sum(d)<=budget:
        return len(d)
    
    for i in range(0, len(d)):
        money += sorted(d)[i]
        if budget - money < 0:
            break
            
    return i
    
