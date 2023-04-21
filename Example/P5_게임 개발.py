# Input
n, m = map(int, input().split())
x, y, z = map(int, input().split())
d = []
for i in range(n):
    row = list(map(int, input().split()))
    d.append(row)
#################################################################################
# Start time
import time
start_time = time.time()
#################################################################################
# Answer
turncnt = 0
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

d[x][y] = 2
cnt += 1

while d:
    if z == 0:
        if d[x-1][y] != 0:
            z += 1
            turncnt += 1
        else:
            x += dx[z]
            y += dy[z]
            d[x][y] = 2
            cnt += 1
    elif z == 1:
        if d[x][y-1] != 0:
            z += 1
            turncnt += 1
        else:
            x += dx[z]
            y += dy[z]
            d[x][y] = 2
            cnt += 1
    elif z == 2:
        if d[x+1][y] != 0:
            z += 1
            turncnt += 1
        else:
            x += dx[z]
            y += dy[z]
            d[x][y] = 2
            cnt += 1
    else:
        if d[x][y+1] != 0:
            z += 1
            turncnt += 1
        else:
            x += dx[z]
            y += dy[z]
            d[x][y] = 2
            cnt += 1
            
    z = z % 4
    
    if turncnt > 3:
        nx = x - dx[z]
        ny = y - dy[z]
        if d[x-1][y] != 0 and d[x+1][y] != 0 and d[x][y-1] != 0 and d[x][y+1] != 0:
            if d[nx][ny] == 1:
                break
            else:
                x = x - dx[z]
                y = y - dy[z]
                d[x][y] = 2
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
