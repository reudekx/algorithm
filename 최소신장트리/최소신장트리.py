'''
제목: 최소 신장 트리와 관련 알고리즘을 알아보자

1) 최소 신장 트리란?
    최소 (비용) 신장 트리 = Minimum Spanning Tree = MST

    신장 트리란?
        그래프의 모든 정점을 포함하고 사이클이 없는 부분 그래프.

    최소 신장 트리란?
        신장 트리 중에서 간선의 가중치 합이 가장 적은 트리.

2) MST를 구하는 알고리즘
    크루스칼 알고리즘, 프림 알고리즘이 존재한다.

    a) 크루스칼 알고리즘 O(E * logV)
        1. 간선들을 가중치를 기준으로 오름차순 정렬한다.
        2. 간선을 하나씩 확인한다.
            해당 간선을 선택함으로써 사이클이 발생하지 않는 경우에만 간선을 선택한다.
        3. V - 1개의 간선이 선택될 때까지 2번을 반복한다. (결과적으로 V개의 정점이 선택됨)

        이때, 사이클의 발생 여부를 확인 하기 위해 '서로소 집합'을 이용하며, union-find 연산을 정의함으로써 구현할 수 있다.
            서로소 집합) 정점들은 한번에 하나의 집합(트리)에만 속한다.
            union 연산) 간선의 두 정점이 속한 집합을 하나로 합친다. (=하나의 트리로 만든다.)
            find 연산) 정점의 소속 집합을 확인한다. (=두 정점에 대해 find 연산을 수행하여,
                만약 동일한 집합에 속해있다면(find(a) == find(b)인 경우) 해당 간선을 선택했을 때 사이클이 발생하게 된다.)

    b) 프림 알고리즘 O((V + E) * logV) = O(E * logV)
        1. 시작 정점을 하나 골라 (0=가중치, 정점)의 형태로 우선순위 큐에 넣는다.
        2. 우선순위 큐에서 가중치가 가장 적은 정점을 하나 꺼내 선택한다. (MST에 포함시킨다.)
        3. 해당 정점의 주위 정점들을 간선 가중치와 함께 우선순위 큐에 넣는다. 
        4. V개의 정점이 선택될 때까지 2, 3번을 반복한다.

        다익스트라 알고리즘과 비슷한 방식으로 구현된다.

기억해야 할 것.
    1. 크루스칼 알고리즘은 유니온-파인드 연산이 필요
    2. 파인드 연산에서 parent값을 재귀적으로 갱신, 유니온 연산에서는 현재 부모만 동기화
    3. 프림 알고리즘은 한번만 방문하는 다익스트라라고 생각
    4. Edge, Node 클래스 정의하면 구현이 편리하고, __lt__ 메서드 적절히 오버라이딩할 것

'''

'''
준비) 일단 먼저 유니온 파인드 먼저 구현해보자

union 함수 안에서 find 함수를 호출하므로 find 함수 먼저 구현.

find 함수의 역할 -> 부모

'''

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

'''
A) 크루스칼 알고리즘
'''

class Edge:
    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

v = 3
e = 3

edges = [
    Edge(0, 1, 1),
    Edge(1, 2, 2),
    Edge(0, 2, 3),
]

def kruskal(v, e, edges):
    edges.sort()

    parent = [i for i in range(v)]
    cnt = 0
    cost = 0

    for edge in edges:
        if find(parent, edge.v1) == find(parent, edge.v2):
            continue
        union(parent, edge.v1, edge.v2)
        cnt += 1
        cost += edge.cost
        if cnt == v - 1:
            break
    
    return cost

print(kruskal(v, e, edges)) # 3

'''
B) 프림 알고리즘
'''

from heapq import heappush, heappop

v = 3
e = 3

class Node:
    def __init__(self, v, cost):
        self.v = v
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

edges = [
    [Node(1, 1), Node(2, 3)],
    [Node(0, 1), Node(2, 2)],
    [Node(1, 2), Node(0, 3)],
]

def prim(v, e, edges):
    visited = [False for _ in range(v)]
    heap = [Node(0, 0)]
    cnt = 0
    cost = 0
    while heap:
        cur = heappop(heap)
        if visited[cur.v]:
            continue
        visited[cur.v] = True
        cnt += 1
        cost += cur.cost
        if cnt == v:
            break
        for nxt in edges[cur.v]:
            if visited[nxt.v]:
                continue
            heappush(heap, nxt)
    return cost

print(prim(v, e, edges))