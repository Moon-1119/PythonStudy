def solution(s):
    temp = int(len(s) / 2)
    
    if len(s) % 2 == 0:
        return s[temp-1] + s[temp]
    else:
        return s[temp]
