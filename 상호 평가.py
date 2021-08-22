def solution(scores):
    answer = ""
    scores = list(map(list, zip(*scores))) # scores의 transpose
    score_mean = 0
    for i, score in enumerate(scores):
        if scores[i][i] == max(score) and score.count(max(score)) == 1:
            score.remove(max(score))
        elif scores[i][i] == min(score) and score.count(min(score)) == 1:
            score.remove(min(score))

        score_mean = sum(score) / len(score)

        if score_mean >= 90:
            answer += "A"
        elif score_mean >=80 and score_mean < 90:
            answer += "B"
        elif score_mean >=70 and score_mean < 80:
            answer += "C"
        elif score_mean >=50 and score_mean < 70:
            answer += "D"
        else:
            answer += "F"
            
    return answer
        
