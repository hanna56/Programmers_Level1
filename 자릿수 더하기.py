def solution(n):
    answer = 0
    for num in map(int, str(n)):
        answer += num

    return answer
