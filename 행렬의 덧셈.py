def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j]+arr2[i][j])

    return answer
  
  

  
# 다른 풀이1
import numpy as np

def solution(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()
  
  
  
# 다른 풀이2
def solution(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j]+=B[i][j]
    return A
