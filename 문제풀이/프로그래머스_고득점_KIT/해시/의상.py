from collections import defaultdict
from math import prod

def solution(clothes):
    cloth_dict = defaultdict(list)
    for cloth, cloth_type in clothes:
        cloth_dict[cloth_type].append(cloth)
    
    answer = prod(len(clothes) + 1 for clothes in cloth_dict.values()) - 1
    return answer

'''
풀이 시간: 6분
접근:
후기:
    from collections import Counter을 이용해서 셀 수 있다.

    cnt = Counter([kind for name, kind in clothes])
'''