def find_upper(s, e):
    if s > e:
        return s
    
    mid = (s + e) // 2

    sum = 0
    for tree in trees:
        sum += max(0, tree - mid)

    if sum < m:
        return find_upper(s, mid - 1)
    else:
        return find_upper(mid + 1, e)



n, m = map(int, input().split())
trees = list(map(int ,input().split()))

print(find_upper(0, max(trees)) - 1)

'''
시작 시간: 21:01
종료 시간: 21:10

접근:
    높이를 0 ~ max(trees)까지 움직인다.

    높이를 1씩 감소시킨다. 잘라낸 합이 M이상이 되는 순간 멈춘다.

    반대로 증가시켜보자.

    합이 M 이상인 높이의 상한을 구한 뒤 1을 빼주면 된다.
    (합이 M미만일 때 멈추므로)
후기:
    랜선 자르기와 거의 동일한 문제였다.
'''