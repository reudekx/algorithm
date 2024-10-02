from collections import defaultdict

def solution(participant, completion):
    cnts = defaultdict(int)
    for p in participant:
        cnts[p] += 1
    for c in completion:
        cnts[c] -= 1
        
    for name, cnt in cnts.items():
        if cnt == 1:
            return name

'''
풀이 시간: 3분
접근:
    동명이인이 있을 수 있다.
후기:
    문제 조건을 잘 읽자.
'''