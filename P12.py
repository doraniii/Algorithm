def solution(s):
    sl=list(s)
    sl.sort(reverse=True)
    return ''.join(sl)