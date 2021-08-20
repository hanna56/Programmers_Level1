def solution(n, arr1, arr2):
    answer = []
    arr = []
    for num in arr1+arr2:
        num_to_two = []
        for i in range(n):
            if num!=0:
                num_to_two.append(num%2)
                num=num//2
            else:
                num_to_two.append(0)
        num_to_two.reverse()
        arr.append(num_to_two)
    
    for i in range(n):
        ans = ""
        for j in range(n):
            if arr[i][j] == 1 or arr[i+n][j] == 1:
                ans += "#"
            else:
                ans += " "
        answer.append(ans)

    return answer
