MOD = 10007

def calc(cur, tops):
    global cnt, cache
    if cur == cnt - 1:
        return 1
    if cur == cnt:
        return 1
    if cur > cnt:
        return 0
    if cache[cur] != -1:
        return cache[cur]
    res = 0
    
    # top이 있는 경우
    
    if cur % 2 != 0 and tops[cur // 2] == 1:
        # 직사각형을 세우거나, 2개의 정사각형으로 채움
        res += 2 * calc(cur + 1, tops) % MOD
        
        # 직사각형을 눞히고 top은 정사각형으로 채움
        res += calc(cur + 2, tops) % MOD
    # top이 없는 경우
    else:
        # 현재 위치를 정사각형으로 채움
        res += calc(cur + 1, tops) % MOD
        # 직사각형을 눞힘
        res += calc(cur + 2, tops) % MOD
    
    cache[cur] = res % MOD
    return res

def bottom_up(cnt, tops):
    for i in range(cnt - 1, -1, -1):
        calc(i, tops)
    
    

def solution(n, tops):
    global cnt, cache
    cnt = 2 * n + 1
    cache = [-1 for _ in range(cnt)]
    
    bottom_up(cnt, tops)
    
    answer = calc(0, tops)
    
    return answer

'''
풀이 시간: 24분
접근:
    한 삼각형과 한 변이 인접한 삼각형을 합치면 마름모가 된다.
    또한 효율성을 위해 DP를 이용해야 한다.
    
    그리고 부분 문제를 만들기 위해 채우는 순서를 강제할 필요가 있다.
    
    일단 뾰족한 부분이 없다고 가정해보자.
    
    이 경우 2n + 1개를 순서대로 선택하면 된다.
    
    뾰족한 부분(이하 top)을 고려해보자.
    
    가령 top의 아래 타일이 채워져 있다면 top은 삼각형으로 정해진다.
    
        여기서 잠깐.. 삼각형이 아니라 사각형과 직사각형이라고 가정해도 문제는 성립한다.
        이 경우 2n + 1개의 밑부분 배열과, 짝수번째마다 top이 존재할 수 있는 윗부분 배열이 된다.
        (index는 0부터 시작하므로 홀수번째)
        이제부터 사각형 문제라고 생각하고 풀어보자.
    
    state를 생각해보자.
    
    (cur) -> 현재 위치가 비어있는 경우 가능한 경우의 수
    
    이렇게 정의한 이유는, 가령 직사각형을 가로로 눞힌 경우
        그 위에 top이 있다면 자동으로 채우고
        cur + 2를 재귀호출하면 되기 때문이다.
        
    어쨌든 cur에서 가능한 여러 조합을 세어주고, 다음 빈 타일을 재귀호출 하면 된다.
        
    
후기:
    삼각형이 등장하여 어렵게 느껴질 수도 있었으나 결국 사각형으로 치환하여 풀 수 있었다.
'''