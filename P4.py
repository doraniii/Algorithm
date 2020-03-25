#체육복
import numpy as np
def solution(n,lost,reserve):
    lost = np.array(lost)
    reserve = np.array(reserve)
    stu = np.ones(n+2)
    
    stu[lost] -= 1
    stu[reserve] += 1
    for i in range(1,n+1):
        if stu[i] == 2 and stu[i-1] == 0:
            stu[i] = stu[i-1] =1
        if stu[i] == 2 and stu[i+1] ==0:
            stu[i] = stu[i+1] =1
    return np.count_nonzero(stu[1:-1])