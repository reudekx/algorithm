from collections import deque

def build_graph(n, edge):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def bfs(n, edge):
    graph = build_graph(n, edge)
    visited = [False for _ in range(n + 1)]
    
    # (node, depth)
    queue = deque()
    queue.append((1, 0))
    visited[1] = True
    
    max_depth = 0
    cnt = 0
    
    while queue:
        cur, depth = queue.popleft()
        if depth > max_depth:
            max_depth = depth
            cnt = 1
        elif depth == max_depth:
            cnt += 1
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append((nxt, depth + 1))
    
    return cnt
    

def solution(n, edge):
    answer = bfs(n, edge)
    return answer


'''
풀이 시간: 8분
접근:
    BFS로 depth를 확인하며 구해보자
후기:
    쉬운 문제였지만 cnt를 세는 게 약간 까다로웠다
    다른 사람의 풀이도 찾아보자.

    다른 사람의 풀이를 확인하니, distance 배열을 이용했다.
    이후 distance.count(max(distance))를 수행해주면 된다.


'''