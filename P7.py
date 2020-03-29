def solution(arr):
    res=[]
    tmp = -1
    for elem in arr:
        if tmp != elem:
            tmp = elem
            res.append(elem)
    return res