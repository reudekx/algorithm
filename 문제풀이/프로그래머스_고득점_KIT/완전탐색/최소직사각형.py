def solution(sizes):
    max_x, max_y = -1, -1
    for x, y in sizes:
        if x < y:
            x, y = y, x
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    answer = max_x * max_y
    return answer


'''
풀이 시간: 3분
접근:
    가로와 세로를 긴 것과 짧은 것으로 나누자.

후기:
'''