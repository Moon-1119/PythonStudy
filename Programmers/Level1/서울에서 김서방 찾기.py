def solution(seoul):
    i = 0
    for lastname in seoul:
        if lastname == "Kim":
            break
        i += 1
    answer = "김서방은 {}에 있다".format(i)
    
    return answer
