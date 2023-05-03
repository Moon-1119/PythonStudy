import numpy as np
def solution(arr):
    answer = []
    for num in arr:
        if answer:
            if num != answer[-1]:
                answer.append(num)
        else:
            answer.append(num)
    return answer
