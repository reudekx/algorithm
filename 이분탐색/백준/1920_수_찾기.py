def find(k, s, e):
    if s > e:
        return False
    mid = (s + e) // 2
    if a[mid] == k:
        return True
    elif a[mid] > k:
        return find(k, s, mid - 1)
    else:
        return find(k, mid + 1, e)




n = int(input())
a = list(map(int, input().split()))
m = int(input())
ks = list(map(int, input().split()))

a.sort()

for k in ks:
    print(int(find(k, 0, len(a) - 1)))

'''
시작 시간: 20:23
종료 시간: 20:27

접근:
    이분탐색으로 해결

후기:
    간단한 문제

'''