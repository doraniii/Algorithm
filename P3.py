#K번째 수
def solution(array, commands):
    res=[]
    res2=[]
    res3=[]
    for i in range(0,len(commands)):
        seq=commands[i]
        res.append(array[seq[0]-1:seq[1]])
        res[i].sort()
        seq2=res[i]
        res2.append(seq[-1])
    for j,k in zip(res,res2):
        res3.append(j[k-1])
    return res3