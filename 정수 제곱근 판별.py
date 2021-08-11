import numpy as np
def solution(n):
    if int(np.sqrt(n)) == np.sqrt(n):
        return (np.sqrt(n)+1)**2
    else:
        return -1
