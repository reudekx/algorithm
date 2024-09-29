MOD = 1000000007
INF = 9999

def is_in_bound(y, x, m, n):
    return y >= 0 and y <= m and x >= 0 and x <= n 

def can_go(y, x, m, n, water):
    return is_in_bound(y, x, m, n) and not water[y][x]

def calc(y, x, cache, m, n, water):
    if not can_go(y, x, m, n, water):
        return (0, INF)
    if y == m and x == n:
        return (1, 1)
    if cache[y][x][0] != -1:
        return cache[y][x]
    
    right = calc(y, x + 1, cache, m, n, water)
    down = calc(y + 1, x, cache, m, n, water)
    
    if right[1] < down[1]:
        cache[y][x] = (right[0], right[1] + 1)
    elif right[1] > down[1]:
        cache[y][x] = (down[0], down[1] + 1)
    else:
        cache[y][x] = ((right[0] + down[0]) % MOD, right[1] + 1)
    
    return cache[y][x]

def solution(m, n, puddles):
    water = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    for y, x in puddles:
        water[y][x] = True
    cache = [[(-1, -1) for _ in range(n + 1)] for _ in range(m + 1)]
    answer = calc(1, 1, cache, m, n, water)[0]
    return answer


'''
풀이 시간: 21분
접근:
    dp[y][x] = min(dp[y][x + 1], dp[y + 1][x]) + 1
    
    문제를 잘못 읽음.. 최단 경로가 아니라 개수를 구해야 했음
    
    dp[y][x] = (경로 개수, 최단 경로)
후기:
    급하게 풀지 말고 문제를 잘 읽고 시작하자..

    또한 애초에 최단 경로를 구하는 것이었으면 중간 과정에서 MOD 연산을 적용하여 답을 구할 수 없음.

'''