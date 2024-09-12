'''
제목: 그래프탐색 알고리즘 정리
(내용이 길어져서 DFS, BFS에 대해서만 작성하고 나머지는 다른 파일로 추후 작성 예정)

그래프탐색 알고리즘의 종류를 나열해보자.

1. DFS
2. BFS
3. 다익스트라
4. 벨만-포드
4. 플로이드-워셜

1) DFS
    재귀 함수 또는 스택을 이용해서 구현 (LIFO 방식 이용)

2) BFS
    큐를 이용해서 구현 (FIFO 방식)

3) 다익스트라 O(ElogV)
    우선순위 큐를 이용해서 구현.
    우선순위 큐는 일반적으로 힙을 이용하여 구현한다.

    heapq 모듈의 heappush, heappop을 이용.

    (노드, 가중치) 쌍을 우선순위 큐에 삽입/추출

4) 벨만-포드 O(VE)
    음의 가중치를 가지는 그래프에 대해서도 사용 가능

5) 플로이드-워셜 O(V^3)
    모든 노드 쌍에 대한 최단경로를 구할 때 사용.


그래프 문제를 풀 때 주의해야 할 점

1) 방문 처리를 적절히 잘 해줘야 한다.
    가령... DFS와 BFS에서 방문에 대한 처리는 어떻게 진행해야 할까?

    크게 2가지 방법으로 나눠볼 수 있을 것 같다.

    a) 자신을 방문했을 때 스스로를 방문(한 것으로) 표시함.
    b) 이전 노드가 자신을 스택/큐에 넣을 때 대신 방문 표시를 해준다.

    DFS의 경우를 생각해보자.
        a의 경우)
            재귀 호출로 구현하는 경우, 가장 일반적인 구현이 아닐까..

            스택을 이용하는 경우에는.. 함수가 복잡해지고 스택에 노드가 중복되어 들어가는 일이 생긴다.
        b의 경우)
            재귀 호출로 구현하는 경우 a의 경우와 동일.
            하지만 최초 호출 시 시작 노드에 대한 방문 표시를 함수 밖에서 해줘야 함..

            스택을 이용하는 경우는 a의 경우보다 적절함.

        따라서 DFS는 그냥 재귀 호출로 구현하고, 방문과 동시에 스스로를 방문 표시하는 것으로..

    BFS의 경우도 생각해보자. BFS는 큐와 반복문을 이용해 구현하는 것이 일반적이다.
        a의 경우)
            스택과 마찬가지로 큐에 노드가 중복되어 들어간다.
        b의 경우)
            가장 적절하다.

        따라서 BFS는 큐에 삽입 전 방문 처리를 하는 것으로 하자.

    결론)
        DFS는 재귀 호출 시 스스로를 방문처리 / BFS는 큐에 삽입 전 미리 방문 처리

    
'''

name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

cnt = len(name)

connected = [
    #A      B      C      D      E      F      G      H      I      J      K
    [False, True,  False, True,  True,  False, False, False, False, False, False],  # A
    [True,  False, True,  True,  False, False, False, False, False, False, False],  # B
    [False, True,  False, False, False, True,  True,  False, False, False, False],  # C
    [True,  True,  False, False, True,  False, False, True,  False, False, False],  # D
    [True,  False, False, True,  False, False, False, True,  True,  False, False],  # E
    [False, False, True,  False, False, False, True,  False, False, True,  False],  # F
    [False, False, True,  False, False, True,  False, False, False, True,  True ],  # G
    [False, False, False, True,  True,  False, False, False, True,  False, True ],  # H
    [False, False, False, False, True,  False, False, True,  False, False, True ],  # I
    [False, False, False, False, False, True,  True,  False, False, False, True ],  # J
    [False, False, False, False, False, False, True,  True,  True,  True,  False]   # K
]

print("     " + " ".join(f"{node:2}" for node in name))
for i, row in enumerate(connected):
    print(f"{name[i]:2}: " + " ".join(f"{cell:2}" for cell in row))

visited = [False for _ in range(cnt)]

def search(fun, start):
    for i in range(cnt):
        visited[i] = False    

    print(f"===== function: {fun.__name__}, start: {name[start]} =====")

    fun(start)


'''
A) DFS

재귀 호출 시 스스로를 방문한 것으로 표시함.
'''

def dfs(cur):
    print(name[cur])
    visited[cur] = True
    for nxt in range(cnt):
        if not connected[cur][nxt]:
            continue
        if visited[nxt]:
            continue
        dfs(nxt)

search(dfs, 0)

'''
B) BFS

큐에 삽입 전 방문한 것으로 표시함.
'''

from collections import deque

def bfs(cur):
    queue = deque()
    queue.append(cur)
    visited[cur] = True
    while queue:
        cur = queue.popleft()
        print(name[cur])
        for nxt in range(cnt):
            if not connected[cur][nxt]:
                continue
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append(nxt)

search(bfs, 0)