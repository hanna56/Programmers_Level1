def solution(n, lost, reserve):
    answer = n-len(lost)
    # 여유분을 갖고 있는 학생 중 도난당한 경우
    for l in sorted(lost):
        if l in reserve:
            answer += 1
            reserve.remove(l)
            lost.remove(l)
    
    # 앞사람만 여유분을 가지고 있거나 뒷사람만 여유분을 가지고 있는 경우
    for l in sorted(lost): 
        reserve.sort()
        if (l-1 in reserve and l+1 not in reserve) or (l-1 not in reserve and l+1 in reserve): 
            answer += 1
            if l-1 in reserve:
                reserve.remove(l-1)
            elif l+1 in reserve:
                reserve.remove(l+1)
            lost.remove(l)

    # 앞뒤사람 모두 여유분을 가지고 있는 경우
    for l in sorted(lost):
        reserve.sort()
        if l+1 in reserve:
            answer += 1
            reserve.remove(l+1)
            lost.remove(l)
        elif l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
            lost.remove(l)
                  
    return answer
