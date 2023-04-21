# Input
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
####################################################
# Start time
import time
start_time = time.time()
####################################################
# Answer
_sum = 0
nums.sort(reverse=True)
maxNum = nums[0]
maxNum1 = nums[1]
i = 0
for j in range(m):
    if i < k:
        _sum += maxNum
        i += 1
    else:
        _sum += maxNum1
        i = 0
print(_sum)
####################################################
# End time
end_time = time.time()
taken_time = end_time - start_time
if taken_time > 1:
  print("Time over")
  print("time :", f"{taken_time :.5f}")
else:
  print("time :", f"{taken_time :.5f}")
####################################################
