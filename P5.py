import calendar
def solution(a, b):
    weekday=calendar.weekday(2016,a,b)
    res=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return res[weekday]