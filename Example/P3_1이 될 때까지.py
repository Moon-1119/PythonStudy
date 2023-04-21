# Input
n, k = map(int, input().split())
####################################################
# Start time
import time
start_time = time.time()
####################################################
# Answer
cnt = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    cnt += 1
print(cnt)
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
