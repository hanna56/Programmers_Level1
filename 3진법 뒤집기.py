def solution(n):
    answer = 0
    num_3 = []
    
    while n!=0:
        num_3.append(n%3)
        n=n//3
    num_3.reverse()

    for i in range(len(num_3)):
        answer+=num_3[i]*3**i
    return answer
