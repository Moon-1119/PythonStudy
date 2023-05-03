def solution(s):
    intList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        for char in s:
            if char not in intList:
                answer = False
    else:
        answer = False
    
    return answer
