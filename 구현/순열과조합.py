'''
순열과 조합

from itertools import permutations, combinations

위 라이브러리를 사용하지 못하는 경우도 있을 수 있으므로, 직접 구현할 줄 알아야 한다.

'''

# 순열
def permutations(arr, n):
    used = [False for _ in arr]
    chosen = []

    def generate():
        if len(chosen) == n:
            yield chosen[:]
            return

        for i in range(len(arr)):
            if used[i]:
                continue
            chosen.append(arr[i])
            used[i] = True
            yield from generate()
            used[i] = False
            chosen.pop()

    return generate()

# 조합
def combinations(arr, n):
    chosen = []

    def generate(start = 0):
        if len(chosen) == n:
            yield chosen[:]
            return
        
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            yield from generate(i + 1)
            chosen.pop()
        
    return generate()

# 중복 순열
def repeated_permutations(arr, n):
    chosen = []

    def generate():
        if len(chosen) == n:
            yield chosen[:]
            return
        
        for i in range(len(arr)):
            chosen.append(arr[i])
            yield from generate()
            chosen.pop()

    return generate()

# 중복 조합
def repeated_combinations(arr, n):
    chosen = []

    def generate(start = 0):
        if len(chosen) == n:
            yield chosen[:]
            return
        
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            yield from generate(i)
            chosen.pop()

    return generate()

# 출력
def debug(func, arr = [1, 2, 3], n = 2):
    print(f"===== {func.__name__} =====")
    for row in func(arr, n):
        print(row)
    
debug(permutations)
debug(combinations)
debug(repeated_permutations)
debug(repeated_combinations)