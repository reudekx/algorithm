def find_upper(s, e):
    if s > e:
        return s
    
    mid = (s + e) // 2

    sum = 0
    for lan in lans:
        sum += lan // mid

    if sum < n:
        return find_upper(s, mid - 1)
    else:
        return find_upper(mid + 1, e)
    

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

lans.sort()

print(find_upper(1, max(lans)) - 1)

'''
시작 시간: 20:41
종료 시간: 20:54

접근:
    '최대' 랜선의 길이를 구해야 한다.
    
    길이가 1이면 랜선의 개수가 최대가 된다.
    길이를 늘려나가면.. 언젠가 랜선의 개수가 N 미만이 된다.
    그러면 그 전의 길이를 선택하면 된다.

    K가 1만이라고 가정할 때,

    길이 l을 이동시키면서 모드 랜선에 대해 몫 연산을 하여
    sum을 구해서 n이상인지 확인.

    n이상인 것 중에서 l의 최대값을 구하자.

    상한을 구한 뒤 1을 빼주면 된다.

후기:
    이분탐색 문제임을 알고 풀었는데 그럼에도 이분탐색을 어떻게
    적용할 것인가를 떠올리는 것이 쉽지는 않았다.
'''