# Input
cards = []
n, m = map(int, input().split())
for i in range(n):
    card = list(map(int, input().split()))
    cards.append(card)
####################################################
# Start time
import time
start_time = time.time()
####################################################
# Answer
minList = []
for card in cards:
    minList.append(min(card))
print(max(minList))
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
