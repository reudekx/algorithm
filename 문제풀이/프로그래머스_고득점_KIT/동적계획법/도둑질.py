# 첫번째 집을 턴 경우
def calc1(cur, cache, money):
    if cur >= len(money) - 1:
        return 0
    if cache[cur] != -1:
        return cache[cur]
    cache[cur] = max(
        calc1(cur + 2, cache, money) + money[cur],
        calc1(cur + 1, cache, money)
    )
    return cache[cur]

# 첫번째 집을 안 턴 경우
def calc2(cur, cache, money):
    if cur > len(money) - 1:
        return 0
    if cache[cur] != -1:
        return cache[cur]
    cache[cur] = max(
        calc2(cur + 2, cache, money) + money[cur],
        calc2(cur + 1, cache, money)
    )
    return cache[cur]

# 재귀 초과 해결용
def bottom_up(cache1, cache2, money):
    for i in range(len(money) - 1, -1, -1):
        calc1(i, cache1, money)
        calc2(i, cache2, money)

def solution(money):
    cache1 = [-1 for _ in range(len(money))]
    cache2 = cache1[:]
    bottom_up(cache1, cache2, money)
    answer = max(calc1(2, cache1, money) + money[0], calc2(1, cache2, money))
    return answer


'''
풀이 시간: 15분
접근:
    문제를 꼼꼼히 읽고 정리해보자.
    
    1) 인접한 집을 털면 안 되므로, 한 칸씩 띄워서 털어야 한다.
    2) 원형으로 배치되있으므로, 첫번째 집의 털이 여부가 마지막 집에 영향을 끼친다.
    
    2번을 어떻게 처리할 것인지?
    가령,
        a) 첫번째 집을 턴 경우
            마지막 집을 절대 털 수 없다.
            두번째 집도 털 수 없다.
        b) 첫번째 집을 안 턴 경우
            마지막 집을 털어도 되고, 안 털어도 된다.
            
    일단 2가지 경우를 나눠서 각각 풀이하면 될 것 같은데..
    
    현재 state를 정의해보자.
    
    현재 cur 위치의 집을 털지말지 결정 중이다.. (결정 중이라는 건 cur - 1을 안 털었다는 뜻)
    max(현재 집을 털었을 때의 최대값, 안 털고 다음 집으로 선택권을 넘겼을 때의 최대값)
후기:
    런타임 에러가 나서 당황했지만 재귀 깊이 제한을 초과한 경우 런타임 에러가 자주 발생했으므로..
    bottom_up 호출을 통해 캐시값을 구해주어 해결함.
    

'''