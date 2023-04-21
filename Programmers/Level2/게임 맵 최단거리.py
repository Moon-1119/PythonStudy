# maps[n][m]이 고립되어 있으면 -1 return 
# -> (n-1,m-1), (n-1,m), (n, m-1) == 0
# 다 돌고 min 값으로 확인 DFS / 최단 거리의 경로로 탐색 BFS
from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    if maps[n-2][m-2] + maps[n-2][m-1] + maps[n-1][m-2] == 0:
        return -1
    else:
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        queue = deque()
        queue.append([0,0])
        
        visited[0][0] = 1 # 시작 point 방문처리
        maps[0][0] = 0
        
        while queue:
            y, x = queue.popleft() # 쌍으로 묶여있는 x, y
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                    if visited[ny][nx] == -1 and not visited[ny][nx]:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append([ny, nx])

        answer = visited[-1][-1]                    
                
    return answer
