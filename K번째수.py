def solution(array, commands):
    answer = []
    for command in commands:
        lst = sorted(array[int(command[0])   - 1 : int(command[1])])
        answer.append(lst[int(command[2])-1])
    
    return answer
