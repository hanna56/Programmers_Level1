def solution(price, money, count):
    prices = sum(range(1,count+1))*price
    return prices-money if prices > money else 0
