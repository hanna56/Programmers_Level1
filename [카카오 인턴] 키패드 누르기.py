def solution(numbers, hand):
    dic = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2),
          7: (2,0), 8: (2,1), 9: (2,2), 0: (3,1)}
    
    answer = ""
    r_location = (3,0)
    l_location = (3,2)
    
    for number in numbers:
        if number in [1,4,7]:
            answer += "L"
            l_location = dic.get(number)
        elif number in [3,6,9]:
            answer += "R"
            r_location = dic.get(number)
        else:
            num_location = dic.get(number)
            r_distance = abs(num_location[0]-r_location[0]) + abs(num_location[1]-r_location[1])
            l_distance = abs(num_location[0]-l_location[0]) + abs(num_location[1]-l_location[1])
            if l_distance == r_distance:
                answer += hand[0].upper()
                if hand[0].upper() == "L":
                    l_location = num_location
                else:
                    r_location = num_location
            elif l_distance > r_distance:
                answer += "R"
                r_location = dic.get(number)
            else:
                answer += "L"
                l_location = dic.get(number)
    return answer
