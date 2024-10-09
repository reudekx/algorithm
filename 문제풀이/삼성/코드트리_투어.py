from heapq import heappush, heappop

INF = 99999999



class Node:
    def __init__(self, v, cost):
        self.v = v
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"(v: {self.v}, cost: {self.cost})"

class Product:
    def __init__(self, ident, revenue, dest):
        self.ident = ident
        self.revenue = revenue
        self.dest = dest

    def __repr__(self):
        return f"(ident: {self.ident}, revenue: {self.revenue}, dest: {self.dest})"

def dijkstra(start):
    dist = [INF for _ in range(n)]
    queue = [Node(start, 0)]

    while queue:
        node = heappop(queue)
        if dist[node.v] < node.cost:
            continue
        dist[node.v] = node.cost
        for nxt in graph[node.v]:
            if dist[nxt.v] < node.cost + nxt.cost:
                continue
            dist[nxt.v] = node.cost + nxt.cost
            heappush(queue, Node(nxt.v, dist[nxt.v]))
    
    return dist

def rebuild_heap():
    global heap
    heap = []
    for product in products.values():
        heappush(heap, (-(product.revenue - cost[product.dest]), product.ident, product))


def add_product(product):
    products[product.ident] = product
    heappush(heap, (-(product.revenue - cost[product.dest]), product.ident, product))

def del_product(ident):
    products.pop(ident, None)

def sell_product():
    if not heap:
        return -1
    neg_earn, ident, best = heap[0]
    while ident not in products:
        heappop(heap)
        if not heap:
            return -1
        neg_earn, ident, best = heap[0]
    if neg_earn > 0:
        return -1
    del_product(ident)
    return ident


q = int(input())
cmd = list(map(int, input().split()))
n, m = cmd[1], cmd[2]
graph = [[] for _ in range(n)]
for i in range(3, len(cmd), 3):
    v, u, w = cmd[i], cmd[i + 1], cmd[i + 2]
    graph[v].append(Node(u, w))
    graph[u].append(Node(v, w))

products = {}
heap = [] # 최소 힙
start = 0
cost = dijkstra(start)

for _ in range(q - 1):
    cmd = list(map(int, input().split()))
    if cmd[0] == 200:
        ident, revenue, dest = cmd[1], cmd[2], cmd[3]
        add_product(Product(ident, revenue, dest))
    elif cmd[0] == 300:
        ident = cmd[1]
        del_product(ident)
    elif cmd[0] == 400:
        ident = sell_product()
        print(ident)
    else: # cmd[0] == 500
        start = cmd[1]
        cost = dijkstra(start)
        rebuild_heap()



'''
풀이 시간: 51분
접근:
    다익스트라 15번 수행하면?

    O(E logV * 15) =  O(1만 * 13 * 15) = 대략 200만

    여행 상품의 최적순위는 힙으로 관리하자.

    존재여부는 사전으로 관리하자.

    추가)
        다익스트라 수행 후 힙을 다시 구성해야 한다.
후기:
    earn은 최대가 되어야 했기 떄문에 음수로 heap에 넣어줬어야 했다.

'''