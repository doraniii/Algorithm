def solution(n):
    nRange=set(range(2,n+1))
    for idx in range(2,n+1):
        if idx in nRange:
            nRange -= set(range(2*idx, n+1, idx))
    return len(nRange)