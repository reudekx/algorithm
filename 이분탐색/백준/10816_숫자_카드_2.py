def find_lower(k, s, e):
    if s > e:
        return s
    mid = (s + e) // 2
    if cards[mid] >= k:
        return find_lower(k, s, mid - 1)
    else:
        return find_lower(k, mid + 1, e)

def find_upper(k, s, e):
    if s > e:
        return s
    mid = (s + e) // 2
    if cards[mid] > k:
        return find_upper(k, s, mid - 1)
    else:
        return find_upper(k, mid + 1, e)    

def count(k):
    upper = find_upper(k, 0, len(cards) - 1)
    lower = find_lower(k, 0, len(cards) - 1)
    return upper - lower


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
tars = list(map(int, input().split()))

cards.sort()

print(*[count(tar) for tar in tars])

'''
시작 시간: 20:31
종료 시간: 20:37

접근:
    이분탐색을 통해 상한/하한을 구한 뒤 상한 - 하한을 반환

후기:
    코드를 복사할 때는 주의하자.
    find_lower 함수를 복사해서 find_upper함수를 작성했는데
    재귀 호출 부분을 수정하지 않아 처음에 출력이 이상하게 나옴

'''