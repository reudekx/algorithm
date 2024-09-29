def calc(i, j, triangle, cache):
    if cache[i][j] != -1:
        return cache[i][j]
    if i == len(triangle) - 1:
        return triangle[i][j]
    cache[i][j] = triangle[i][j] + max(
        calc(i + 1, j, triangle, cache),
        calc(i + 1, j + 1, triangle, cache)
    )
    return cache[i][j]

def solution(triangle):
    cache = [[-1 for _ in range(i + 1)] for i in range(len(triangle))]
    answer = calc(0, 0, triangle, cache)
    return answer


'''
풀이 시간: 5분 30초
접근:
    dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
후기:
    간단한 문제였음
'''