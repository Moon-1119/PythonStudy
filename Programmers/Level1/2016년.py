def solution(a, b):
    dayList = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    totalDay = 0
    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]
    
    for i in range(1, a):
        if i == 2:
            days = 29
            totalDay += days
        elif i in d31:
            days = 31
            totalDay += days
        else:
            days = 30
            totalDay += days
        
    totalDay += b
    index = totalDay % 7
    print(index)
    
    return dayList[index]
