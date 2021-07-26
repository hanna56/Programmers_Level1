#내풀이
def solution(nums):
    if len(nums)/2 < len(set(nums)):
        return len(nums)/2
    else:
        return len(set(nums))
      
      
      
      
#모범답안
def solution(nums):
    return min(len(set(nums)), len(nums)//2)
