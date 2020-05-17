def solution(n):
    a=str(n)
    answer=[]
    for i in range(0,len(a)):
        answer.append(int(a[i]))
    return answer[::-1]