def solution(arr,d):
    res = []
    for i in arr:
        if i%d == 0:
            res.append(i)
            res.sort()
    if res ==[]:
        return [-1]
    return res
