def solution(s):
    a=[]
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2 ==0:
                a.append(s[i][j].upper())
            else: a.append(s[i][j].lower())
        a.append(" ")
    res="".join(a[:-1])
    return res