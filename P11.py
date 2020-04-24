def solution(py):
    res=py.upper()
    P=0
    Y=0
    for i in res:
        if i=='P': P+=1
        elif i=='Y': Y+=1
        else: pass
    
        return True if P==Y else False