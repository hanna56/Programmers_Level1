def solution(answers):
    count_a = 0
    count_b = 0
    count_c = 0
    answer = []

    a = [1,2,3,4,5] 
    b = [2,1,2,3,2,4,2,5] 
    c = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            count_a += 1
        if answers[i] == b[i%8]:
            count_b += 1
        if answers[i] == c[i%10]:
            count_c += 1
    max_count = max([count_a, count_b, count_c])

    if count_a == max_count:
      answer.append(1)
    if count_b == max_count:
      answer.append(2)
    if count_c == max_count:
      answer.append(3)

    return answer
  
  
  
  
  # 다른 풀이
  def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
