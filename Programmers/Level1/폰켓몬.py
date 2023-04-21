import numpy as np
def solution(nums):
    getNum = len(nums) // 2
    uniqueNums = np.unique(nums)
    if len(uniqueNums) < getNum:
        return len(uniqueNums)
    else:
        return(getNum)
