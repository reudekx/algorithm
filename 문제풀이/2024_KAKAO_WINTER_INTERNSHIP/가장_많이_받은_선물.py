def build_index(friends):
    index = {}
    for idx, friend in enumerate(friends):
        index[friend] = idx
    return index

def build_diffs(index, gifts):
    diffs = [[0 for _ in range(len(index))] for _ in range(len(index))]
    for gift in gifts:
        a, b = gift.split()
        ia, ib = index[a], index[b]
        diffs[ia][ib] += 1
        diffs[ib][ia] -= 1
    return diffs

def build_factors(diffs):
    factors = [0 for _ in range(len(diffs))]
    for i, diff in enumerate(diffs):
        factors[i] = sum(diff)
    return factors

def build_next_month(diffs, factors):
    next_month = [0 for _ in range(len(diffs))]
    for i in range(len(diffs)):
        for j in range(i + 1, len(diffs[0])):
            if diffs[i][j] > 0:
                next_month[i] += 1
            elif diffs[i][j] < 0:
                next_month[j] += 1
            elif factors[i] > factors[j]:
                next_month[i] += 1
            elif factors[i] < factors[j]:
                next_month[j] += 1
    return next_month
            

def solution(friends, gifts):
    answer = 0
    index = build_index(friends)
    diffs = build_diffs(index, gifts)
    factors = build_factors(diffs)
    next_month = build_next_month(diffs, factors)
    answer = max(next_month)
    return answer


'''
풀이 시간: 19분
접근:
    문제 파악.
    
    선물 차 / 선물 지수의 비교 후 각각의 친구들로부터 선물을 주거나 받는다.
    이때 선물을 가장 많이 받는 사람의 선물 받은 수를 구하여랴.
후기:
    집중에서 풀지 않으면 수렁으로 빠질 수도..
    변수명에서 좀 더 정보가 드러나도록 하든가 아니면 주석을 적절히 적으면서 푸는 게 좋을 것 같다.
    또한 개수를 n으로 구해서 푸는 게 나았을 수도

    그리고 전역변수를 적절히 설정해서 쓰자 (무분별한 사용은 지양하는 게 좋겠지만, 코테를 통과해야하니까..)
'''