


DIRS = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]


class Knight:
    def __init__(self, name, r, c, h, w, k):
        self.name = name
        self.y = r
        self.x = c
        self.h = h
        self.w = w
        self.max_hp = k
        self.hp = k
        self.is_alived = True
        self.is_visited = False

    def __repr__(self):
        return f"({self.name}, {self.y}, {self.x}, {self.hp})"

knights = []

# class Line:
#     def __init__(self, y, x, crds):
#         self.y = y
#         self.x = x
#         self.crds = crds


def is_in_bound(y, x):
    return y >= 0 and y < L and x >= 0 and x < L

def is_valid(y, x):
    return is_in_bound(y, x) and board[y][x] != 2

# 이동시 도달하는 새로운 줄의 좌표 목록을 반환
def get_next_line(knight, direction):
    dy, dx = DIRS[direction]
    line = []
    if dy == 0:
        if dx > 0:
            nx = knight.x + knight.w + dx - 1
        else:
            nx = knight.x + dx
        for y in range(knight.y, knight.y + knight.h):
            line.append((y, nx))
        return line
    else:
        if dy > 0:
            ny = knight.y + knight.h + dy - 1
        else:
            ny = knight.y + dy
        for x in range(knight.x, knight.x + knight.w):
            line.append((ny, x))
        return line
    return None

# line이 기사와 겹치는지 확인
def is_in_line(knight, line):
    for y, x in line:
        if y >= knight.y and y < knight.y + knight.h and x >= knight.x and x < knight.x + knight.w:
            return True
    return False

def damage(knight):
    for y in range(knight.y, knight.y + knight.h):
        for x in range(knight.x, knight.x + knight.w):
            if board[y][x] == 1:
                knight.hp -= 1

    if knight.hp <= 0:
        knight.is_alived = False

# 갈 수 있는 위치인지 확인
# 생각해보니까 한 줄만 체크하면 될 것 같은데..
def can_move(line):
    for y, x in line:
        if not is_valid(y, x):
            return False
    return True

# 한 칸 이동
def move(knight, direction):
    dy, dx = DIRS[direction]
    knight.y += dy
    knight.x += dx

def get_pushables(knight, direction):
    line = get_next_line(knight, direction)
    knight.is_visited = True

    pushable = [knight]

    # 벽으로 막혔는지 확인
    if not can_move(line):
        return []

    # 연쇄적으로 밀릴 기사 구하기
    next_knights = []
    for next_knight in knights:
        if not next_knight.is_visited and next_knight.is_alived and is_in_line(next_knight, line):
            next_knights.append(next_knight)
            next_knight.is_visited = True

    # 다음 기사들 밀어보고 하나라도 안 밀리면 중단
    for next_knight in next_knights:
        next_pushable = get_pushables(next_knight, direction)
        if not next_pushable:
            return []
        pushable.extend(next_pushable)

    return pushable

def push(knight, direction):
    pushables = get_pushables(knight, direction)
    # print("====pushables====")
    # print(pushables)
    for i, knight in enumerate(pushables):
        move(knight, direction)
        if i != 0:
            damage(knight)
    # print("====knights after push====")
    # print(knights)

L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]

for i in range(N):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    knights.append(Knight(i, r, c, h, w, k))

for _ in range(Q):
    i, d = map(int, input().split())
    knight = knights[i - 1]
    if not knight.is_alived:
        continue

    for k in knights:
        k.is_visited = False

    push(knight, d)

damage_sum = 0

for knight in knights:
    if not knight.is_alived:
        continue
    damage_sum += knight.max_hp - knight.hp

print(damage_sum)

'''
풀이 시간: 1시간 30분
접근:
    '생존한' 기사들이 총 받은 대미지의 합을 구해야 한다.
    -> 사망한 기사들은 제외

    move 함수를 구현하는 게 핵심이다.

    dir로 밀게 되면..
        일단 벽만 고려했을 때,
            벽이 없으면 dir로 한 칸 이동하게 된다.
        이제 다른 기사를 고려하면,
            i번째 기사의 경로 상에 있는 기사들을 밀어야 한다.
        
        이를 재귀적으로 반복해야 한다.

    즉,

    특정 방향으로 갈 수 있는지 먼저 따지고,
    
    갈 수 있으면,
        목적지에 있는 다른 기사들에 대해 재귀 호출

    갈 수 없으면 그냥 종료


    생각해보니까, 밀 수 있는 기사들을 모아서 한번에 밀어야 함.

시간 복잡도:
    매 명령마다 모든 기사를 따지면.. 100 * 30 * 30 -> 시간 충분


후기:
    방문 처리를 안 해서 오류가 났었고,
    변수명을 실수로 동일하게 설정하여 디버깅이 어려웠다.

    가령, knight변수를 이미 쓰는 도중 for knight in knights와 같이 코드를 적어 덮어씌어진다든지..
'''