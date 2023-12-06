# 14940, 쉬운 최단 거리
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

field = []
for i in range(N):
    coor = list(map(int, sys.stdin.readline().strip().split()))
    field.append(coor)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visit_ = [[False for j in range(M)] for k in range(N)]

def bfs(x, y):
    dq = deque([])
    if not visit_[y][x]:
        dq.append([x, y, 0])
        visit_[y][x] = True
    while dq:
        x, y = dq.popleft()
        visit_[y][x] = True

        field[y][x] = coor[2]
        for dt in range(4):
            moved_x = x + dx[dt]
            moved_y = y + dy[dt]
            if 0 <= moved_x < M and 0 <= moved_y < N:
                if field[moved_y][moved_x] == 1 and not visit_[moved_y][moved_x]:
                    dq.append((moved_x, moved_y, coor[2]+1))
                    visit_[moved_y][moved_x] = True

count = 0
for i in range(len(field)):
    if count == 1:
        break
    for j in range(M):
        if field[i][j] == 2:
            bfs(j, i)
            count = 1
            break


for i in range(len(field)):
    for j in range(M):
        if field[i][j] == 1 and not visit_[i][j]:
            field[i][j] = -1
for i in field:
    for j in i:
        sys.stdout.write(f"{j} ")
    sys.stdout.write(