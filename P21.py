def solution(n):
    a=str(n)
    b=[]
    for i in range(len(a)):
        b.append(int(a[i]))
    return sum(b)
