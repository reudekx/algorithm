def calc(dp, a, b):
    for left in dp[a]:
        for right in dp[b]:
            dp[a + b].append(left + right)
            dp[a + b].append(left - right)
            dp[a + b].append(left * right)
            if right != 0:
                dp[a + b].append(left // right)

def solution(N, number):
    dp = [[] for i in range(9)]
    
    for i in range(1, 9):
        dp[i].append(int(str(N) * i))
        
    for i in range(2, 9):
        for j in range(1, i):
            calc(dp, j, i - j)
    
    for i in range(1, 9):
        if number in dp[i]:
            return i
    
    return -1

'''
풀이 시간: 30분
접근:
후기:
    고민을 좀 많이 했는데 결국 정공법으로 해결함.
    다만 중복된 값 등에 대한 처리를 안 했는데 통과됨..
    -> 시간복잡도를 미리 계산해서 위처럼 풀어도 되었다는 것을 빠르게 파악했어야 했다.

    추가) 배열 대신 set를 이용했으면 훨씬 효율적인 풀이가 가능했을 것이다. 아래는 set를 이용한 개선 버전

'''

def calc(dp, a, b):
    for left in dp[a]:
        for right in dp[b]:
            dp[a + b].add(left + right)
            dp[a + b].add(left - right)
            dp[a + b].add(left * right)
            if right != 0:
                dp[a + b].add(left // right)

def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    if number in dp[1]:
        return 1
        
    for i in range(2, 9):
        for j in range(1, i):
            calc(dp, j, i - j)
        
        if number in dp[i]:
            return i
    
    return -1