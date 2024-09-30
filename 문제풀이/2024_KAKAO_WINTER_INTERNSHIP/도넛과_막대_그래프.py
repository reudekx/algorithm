import sys
sys.setrecursionlimit(1000000)

def dfs(cur):
    global graph, visited
    visited[cur] = True
    cycle = 0
    for nxt in graph[cur]:
        if visited[nxt]:
            cycle += 1
        else:
            cycle += dfs(nxt)
    return cycle
    
        
def solve():
    global cnt, graph, start, visited
    
    visited = [False for _ in range(cnt + 1)]
    stick = 0
    donut = 0
    eight = 0
    for node in graph[start]:
        cycle = dfs(node)
        if cycle == 0:
            stick += 1
        elif cycle == 1:
            donut += 1
        else:
            eight += 1
    return [start, donut, stick, eight]
    
def solution(edges):
    global cnt, graph, start
    cnt = max(max(edge) for edge in edges)
    graph = [[] for _ in range(cnt + 1)]
    target = set()
    for v1, v2 in edges:
        graph[v1].append(v2)
        target.add(v2)
    for i in range(1, cnt + 1):
        if i not in target and len(graph[i]) >= 2:
            start = i
            break

    answer = solve()
    return answer

'''
풀이 시간: 1시간 도전 후 실패 -> 다음날 통과
접근:
후기:
    start 정점을 식별해야 한다는 것은 떠올릴 수 있었다.
    다만 start 정점의 조건 중 in-degree가 0이라는 것만 처리하고 out-degree가 2이상이어야 한다는 것을 망각했다..
    (이 경우 시작 정점이 막대 그래프의 중간 부분을 가리키면, 해당 막대 그래프의 root는 in-degree가 0이다)

    그래서 dfs함수가 잘못된 줄 알고 한참을 디버깅 및 코드 수정 하였지만 실패함.
    
    다음날 처음부터 코드를 다시 작성하니 start 정점 조건 중 빼먹은 것을 발견하여 문제를 풀 수 있었다.
    
    또한 애초에 예시를 잘 확인했으면 내가 틀렸다는 것을 알 수 있었다.

    결론:
        조건을 파악했으면, 혹시 틀리지 않았나 예시를 통해 한번 검증해볼 필요가 있다.

'''