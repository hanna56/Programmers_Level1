def gcd(X,Y):
    while(Y):
        X,Y = Y, X % Y
    return X

def lcm(X,Y):
    return X*Y/gcd(X,Y)

def solution(n, m):
    return [gcd(n,m), lcm(n,m)]
