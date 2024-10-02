def build_graph(n, wires):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def init_visited(visited):
    for i in range(len(visited)):
        visited[i] = False

def solve(n, wires):
    graph = build_graph(n, wires)
    visited = [False for _ in range(n + 1)]
    
    def dfs(cur):
        visited[cur] = True
        cnt = 1
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            cnt += dfs(nxt)
        return cnt
        
    diff = 100
    
    for v1, v2 in wires:
        init_visited(visited)
        visited[v2] = True
        v1_cnt = dfs(v1)
        init_visited(visited)
        visited[v1] = True
        v2_cnt = dfs(v2)
        diff = min(diff, v1_cnt - v2_cnt if v1_cnt > v2_cnt else v2_cnt - v1_cnt)
    
    return diff

def solution(n, wires):
    answer = solve(n, wires)
    return answer

'''
풀이 시간: 7분
접근:
    2중 for문 돌려도 1만번이라 널널함.
    
    각 간선에 대해 양쪽으로 dfs를 돌려 개수를 센뒤 저장하자.
후기:

'''