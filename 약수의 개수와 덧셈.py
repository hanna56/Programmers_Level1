def solution(left, right):
    count = 0
    answer = 0
    
    for num in range(left, right+1):
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
        count = 0
    return answer
