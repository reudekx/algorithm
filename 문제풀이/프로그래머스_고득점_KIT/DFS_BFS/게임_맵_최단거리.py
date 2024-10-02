from collections import deque

DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def is_in_bound(y, x):
    return y >= 0 and y < n and x >= 0 and x < m

def can_go(y, x, maps):
    return is_in_bound(y, x) and maps[y][x] == 1

def bfs(maps):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    while queue:
        y, x, dist = queue.popleft()
        if y == n - 1 and x == m - 1:
            return dist
        for dy, dx in DIRS:
            ny, nx = y + dy, x + dx
            if not can_go(ny, nx, maps):
                continue
            if visited[ny][nx]:
                continue
            queue.append((ny, nx, dist + 1))
            visited[ny][nx] = True
    return -1

def solution(maps):
    global n, m
    n = len(maps)
    m = len(maps[0])
    answer = bfs(maps)
    return answer if answer <= 99999 else -1

'''
후기:
    2차원 배열에서 최단 경로 찾는 문제는 BFS 활용
'''