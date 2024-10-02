def dfs(cur, res, numbers, target):
    if cur == len(numbers):
        return int(res == target)
    res = dfs(cur + 1, res + numbers[cur], numbers, target) \
        + dfs(cur + 1, res - numbers[cur], numbers, target)
    return res
    

def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer

'''
접근:
    인자로 연산 결과를 넘겨야 함

'''