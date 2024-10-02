from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

DIR = {
    0: (-1, 0),
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (1, -1),
    6: (0, -1),
    7: (-1, -1),
}

def build_graph(arrows):
    graph = defaultdict(set)
    cur = (0, 0)
    for arrow in arrows:
        nxt = (cur[0] + DIR[arrow][0], cur[1] + DIR[arrow][1])
        graph[cur].add(nxt)
        nxt_nxt = (nxt[0] + DIR[arrow][0], nxt[1] + DIR[arrow][1])
        graph[nxt].add(nxt_nxt)
        cur = nxt_nxt
    return graph

def solve(arrows):
    graph = build_graph(arrows)
    visited = set()
    edge = set()
    
    def dfs(cur):
        visited.add(cur)
        cycle = 0
        for nxt in graph[cur]:
            if cur + nxt in edge:
                continue
            edge.add(cur + nxt)
            edge.add(nxt + cur)
            if nxt in visited:
                cycle += 1
                continue
            cycle += dfs(nxt)
        return cycle
    
    return dfs((0, 0))
    

def solution(arrows):
    answer = solve(arrows)
    return answer

'''
풀이 시간: 45분 (힌트를 참고함..)
접근:
    문제 자체가 잘 이해가 안 가는데..
    일단 예시에서 큰 사각형이 하나의 방이라는데
    이게 모양은 큰 사각형이지만 실제로는 U자 모양의 하나의 도형인 건가?
        즉 편의를 위해 큰 사각형이라고 한 걸 수도..?
        
    그렇다고 치면,
    
    그래프의 사이클 수를 찾는 문제 같은데?
    
    일단 그래프를 먼저 생성하고, DFS를 통해 사이클 수를 세보자

후기:
    틀리는 이유를 모르겠어서 인터넷을 참고해서 예외 조건을 알아내었다.

    1. 그렸던 선을 다시 그을 수 있음.
        가령 (0, 0)에서 (1, 1)로 갔다가, 다시 (0, 0)으로 돌아오는 경우..
        가상의 그래프에서는 사이클이겠지만 이 문제에서의 도형은 아니다.
        따라서 간선의 방문도 체크해야 한다.
        
    2. 2 by 2 크기에서 모래시계 모양을 그리면 도형이 1개로 식별됨
        좌표 문제에서 자주 발견되는 함정이다.
        이런 경우 좌표를 2배해서 해결함.


'''