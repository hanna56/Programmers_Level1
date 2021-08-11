import numpy as np
def solution(n):
    return (np.sqrt(n)+1)**2 if int(np.sqrt(n))==np.sqrt(n) else -1
