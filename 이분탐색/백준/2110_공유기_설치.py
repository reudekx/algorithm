def find_upper(s, e):
    if s > e:
        return s
    
    mid = (s + e) // 2

    cnt = 1
    pre_i = 0
    for i in range(1, n):
        if pos[i] - pos[pre_i] >= mid:
            cnt += 1
            pre_i = i
    if cnt < c:
        return find_upper(s, mid - 1)
    else:
        return find_upper(mid + 1, e)


n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]

pos.sort()

print(find_upper(0, 1000000000) - 1)

'''
시작 시간: 21:14
종료 시간: 21:37

접근:
    어디에 설치할지 기준점을 찾아야 한다.
    첫번째 집에 설치해야 하는 것은 타당해보인다.

    최소 인접 거리가 최대값보다 더 큰 경우에는 C - 2개의 공유기를
    모두 설치할 수 없다는 뜻이다.

    최소 인접 거리를 이동시키며 이분탐색을 수행할 수 있다.

    다만 최소 인접 거리를 어떻게 구할 것인가?

    첫번째 공유기를 기준으로 최소 인접 거리 이상인 지점마다
    하나씩 설치하면 됨. 그래서 C - 1개를 꽂을 수 있는지 확인하면 된다.
    
    다음 위치 - 직전 위치 >= 최소 인접 거리인 경우를 카운트 증가
    및 직전 위치를 다음 위치로 갱신해주자

    카운트가 C보다 크거나 같은 경우의 상한을 구해서, 1을 빼주자

후기:
    pos 리스트를 정렬 안 해서 10분 정도 더 소모한 것 같다..
    항상 정렬을 잊지 말자

'''