'''
순열과 조합

from itertools import permutations, combinations

위 라이브러리를 사용하지 못하는 경우도 있을 수 있으므로, 직접 구현할 줄 알아야 한다.

1) 순열
    used 배열 이용
2) 조합
    한 원소를 선택했으면, 그 다음 인덱스 중에서 선택
3) 중복 순열
    조건 없이 반복하여 n개 선택
4) 중복 조합
    한 원소를 선택했으면, 해당 원소의 인덱스를 포함하여 다음 인덱스 중에서 선택

공통)
    generator 함수를 정의하여 이를 실행하여 생성된 객체를 반환하는 wrapper 함수 구현하면 됨.

각각의 규칙을 외울 필요는 없고, chosen 배열을 하나씩 채워넣는다는 것만 기억하면 됨
    
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