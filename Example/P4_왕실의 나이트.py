# Input
input_data = input()
x = int(input_data[1])
y = int(ord(input_data[0])) - int(ord("a")) + 1
#################################################################################
# Start time
import time
start_time = time.time()
#################################################################################
# Answer
cnt = 0
start = [x, y]
move = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
for m in move:
  temp = [0, 0]
  temp[0] = start[0] + m[0]
  temp[1] = start[1] + m[1]
  print(temp)
  if temp[0] >= 1 and temp[0] <= 8 and temp[1] >= 1 and temp[1] <= 8:
    cnt += 1
  else:
    continue
print(cnt)
#################################################################################
# End time
end_time = time.time()
taken_time = end_time - start_time
if taken_time > 1:
  print("Time over")
  print("time :", f"{taken_time :.5f}")
else:
  print("time :", f"{taken_time :.5f}")
#################################################################################
