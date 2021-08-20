def solution(s, n):
    answer = ""
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    
    for a in s:
        if a == " ":
            answer += " "
        elif a.islower():
            answer += low[(low.index(a)+n)%len(low)]
        else:
            answer += up[(up.index(a)+n)%len(up)]
            
    return answer
