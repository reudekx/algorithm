from itertools import combinations, product

def find_lower(arr, k, s, e):
    if s > e:
        return s
    mid = (s + e) // 2
    if arr[mid] >= k:
        return find_lower(arr, k, s, mid - 1)
    return find_lower(arr, k, mid + 1, e)

def calc_win(dice, comb):
    a_dice = [dice[c] for c in comb]
    b_dice = [dice[i] for i in range(len(dice)) if i not in comb]
    
    a_sums = sorted(list(sum(p) for p in product(*a_dice)))
    b_sums = sorted(list(sum(p) for p in product(*b_dice)))
    
    win = 0
    for a_sum in a_sums:
        win += find_lower(b_sums, a_sum, 0, len(b_sums) - 1)
    
    return win
    
def solve(dice):
    combs = list(combinations(range(len(dice)), len(dice) // 2))
    wins = [calc_win(dice, comb) for comb in combs]
    idx = wins.index(max(wins))
    res = sorted([dice + 1 for dice in combs[idx]])
    return res

def solution(dice):
    answer = solve(dice)
    return answer

'''
풀이 시간: 1시간 이상
접근:
후기:
    이분탐색을 떠올리지 못한 채 완전탐색은 불가능하다고 생각했다.

    comb가 최대 252개 존재하고,
    calc_win 내부에서
    a_sums가 6^5가지 존재하고..

    이때 이분탐색을 통해 b_sums와 곱연산을 하면

    6^5 * log(6^5) ..

    이분탐색을 하지않으면 252 * 6^10이지만 이분탐색 덕분에 시간복잡도가 줄어든다.

    또한 comb에 대해 나머지 여집합을 구해줘야 하는데,
    그렇게 안 하고 나머지 comb들에 대해 모두 계산해버려서 계속 잘못된 답이 나왔었다.

'''