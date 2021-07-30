def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine', 'ten']
    
    for idx, n in enumerate(num):
        if n in s:
            s = s.replace(n, str(idx))
            
    return int(s)
