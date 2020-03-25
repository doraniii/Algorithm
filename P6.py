#가운데 글자 가져오기
import math
def solution(s):
    if len(s)%2==0:
        return s[int((len(s)-1)/2):int((len(s)-1)/2)+2]
    else:
        return s[math.ceil(len(s)/2)-1]