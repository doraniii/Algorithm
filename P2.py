#모의고사
from itertools import cycle
import numpy as np
def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    seq = zip(cycle(p1),cycle(p2),cycle(p3))
    res=np.zeros(3)
    
    for sol in answers:
        tmp = np.array(next(seq))
        res[tmp==sol]+=1
        
    cnt = np.count_nonzero(res[res==res.max()])
    if not cnt:
        return []
    
    res = res.argsort()+1
    return list(res[3-cnt:])
print(solution([1,2,3,4,5]))