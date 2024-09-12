'''
제목 : 다익스트라 알고리즘 정리

다익스트라 알고리즘 설명
    1) 음의 가중치가 없는 그래프에서 시작 노드로부터 다른 모든 노드까지의 최단 경로들을 구할 수 있다.
    2) 우선순위 큐를 이용한다. python의 경우 heapq 모듈의 heappush, heappop 함수를 사용하면 됨
'''

INF = 9999

name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

cnt = len(name)

graph = {
    0: {1: 4, 2: 2, 5: 3},
    1: {3: 3, 4: 1, 7: 6},
    2: {1: 1, 3: 5, 5: 2},
    3: {4: 2, 6: 4},
    4: {7: 3},
    5: {6: 1},
    6: {7: 2},
    7: {}
}

'''
다익스트라 함수 구현
'''
from dataclasses import dataclass
from heapq import heappush, heappop


def dijkstra(cur):
    dist = [INF for _ in range(cnt)]
    queue = [(0, cur)]
    while queue:
        cost, cur = heappop(queue)
        if cost > dist[cur]:
            continue
        dist[cur] = cost
        for nxt, ncost in graph[cur].items():
            if cost + ncost > dist[nxt]:
                continue
            dist[nxt] = cost + ncost
            heappush(queue, (dist[nxt], nxt))
    return dist

dist = dijkstra(0)
print(dist)