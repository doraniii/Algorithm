def solution(a, b):
    if a > b :
        a = sum(range(b,a+1))
    else :
        a = sum(range(a,b+1))
    return a