def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for k in range(len(board)):
            if board[k][move-1] > 0:
                basket.append(board[k][move-1])
                board[k][move-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += 2
                    basket = basket[:-2]
                break
                
    return answer
