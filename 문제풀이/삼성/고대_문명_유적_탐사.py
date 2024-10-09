def print_matrix(matrix):
    for row in matrix:
        print(row)

def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

def horizontal_flip(matrix):
    return [row[::-1] for row in matrix]

def vertical_flip(matrix):
    return matrix[::-1]

def rotate_0(matrix):
    return matrix[:]

def rotate_90(matrix):
    return horizontal_flip(transpose(matrix))

def rotate_180(matrix):
    return vertical_flip(horizontal_flip(matrix))

def rotate_270(matrix):
    return vertical_flip(transpose(matrix))
    
ROTATE_FUNCS = [
    rotate_0, rotate_90, rotate_180, rotate_270
]

def rotate_part(y, x, relics, rotate_func):
    relics = [row[:] for row in relics]
    part_matrix = [row[x - 1:x + 2] for row in relics[y - 1:y + 2]]
    rotated_part_matrix = rotate_func(part_matrix)
    for i, row in enumerate(rotated_part_matrix):
        relics[y - 1 + i][x - 1:x + 2] = row
    return relics

DIRS = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def is_in_bound(y, x):
    return y >= 0 and y < 5 and x >= 0 and x < 5

def count_relic(y, x, relics, visited):
    visited[y][x] = True
    cnt = 1
    for dy, dx in DIRS:
        ny, nx = y + dy, x + dx
        if not is_in_bound(ny, nx) or visited[ny][nx] or relics[ny][nx] != relics[y][x]:
            continue
        cnt += count_relic(ny, nx, relics, visited)
    return cnt

def remove_relic(y, x, kind, relics):
    relics[y][x] = 0
    for dy, dx in DIRS:
        ny, nx = y + dy, x + dx
        if not is_in_bound(ny, nx) or relics[ny][nx] != kind:
            continue
        remove_relic(ny, nx, kind, relics)

def gain_once(relics):
    visited = [[False for _ in range(5)] for _ in range(5)]
    cnt_sum = 0
    for y in range(5):
        for x in range(5):
            if visited[y][x] or relics[y][x] == 0:
                continue
            cnt = count_relic(y, x, relics, visited)
            if cnt >= 3:
                cnt_sum += cnt
                remove_relic(y, x, relics[y][x], relics)

    return cnt_sum

def fill_relics(relics, news, news_idx):
    for x in range(0, 5):
        for y in range(4, -1, -1):
            if relics[y][x] != 0:
                continue
            relics[y][x] = news[news_idx]
            news_idx += 1
            if news_idx == len(news):
                return news_idx
    return news_idx

def process_turn(relics, news, news_idx):
    max_gain = 0
    max_state = None
    for rotate_func in ROTATE_FUNCS:
        for x in range(1, 4):
            for y in range(1, 4):
                rotated = rotate_part(y, x, relics, rotate_func)
                gain = gain_once(rotated)
                if gain > max_gain:
                    max_gain = gain
                    max_state = rotated
    if max_gain == 0:
        return max_gain, max_state, news_idx
    while news_idx < len(news):
        news_idx = fill_relics(max_state, news, news_idx)
        gain = gain_once(max_state)
        if gain == 0:
            break
        max_gain += gain

    return max_gain, max_state, news_idx

def solve(relics, news, k):
    gain_per_turn = []
    turn = 0
    news_idx = 0
    while turn != k:
        cur_gain, relics, news_idx = process_turn(relics, news, news_idx)
        if cur_gain == 0:
            break
        gain_per_turn.append(cur_gain)
        turn += 1
    return gain_per_turn

k, m = map(int, input().split()) 
relics = [list(map(int, input().split())) for _ in range(5)]
news = list(map(int, input().split()))

print(*solve(relics, news, k))


'''
풀이 시간: 1시간 34분
접근:
    5 by 5
    7가지 유물

    완전탐색을 진행하자.

후기:
    회전 함수 구현을 어느정도 암기했기에 시간이 많이 단축되었다.

    또한 일부 테스트 케이스를 통과하지 못해 오류를 찾느라 시간이 오래 걸렸는데..
        문제 조건을 제대로 구현하지 않은 게 실수였다.

        1. k턴만 진행해야 했는데, 계속 진행하였다.

        2. 회전을 택하는 방법에서.. 우선순위를 잘못 설정했다. (이중 for문의 outer와 inner가 뒤바뀌어 있었다.)

    다음부터는 문제를 풀 때 조건을 꼼꼼하게 읽고 잘 구현했나 따져봐야겠다.

'''