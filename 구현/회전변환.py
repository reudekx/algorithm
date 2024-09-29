'''
2차원 배열의 회전변환에 대해 정리해보자.

transpose와 flip 함수를 조합하여 rotate함수를 구현할 수 있다.

가령 (시계방향으로) 90도 회전인 경우, transpose후 horizontal flip을 수행하면 된다.

추가)
    transpose 함수의 경우 matrix를 각 원소(row)들로 분해하여 zip 함수를 통해 열을 행으로 변환할 수 있다. -> 이게 더 쉬운 방법
'''


def transpose(matrix):
    # return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return [list(row) for row in zip(*matrix)]

def horizontal_flip(matrix):
    # return [matrix[i][::-1] for i in range(len(matrix))]
    return [row[::-1] for row in matrix]

def vertical_flip(matrix):
    return matrix[::-1]

def rotate_90(matrix):
    return horizontal_flip(transpose(matrix))

def rotate_180(matrix):
    return vertical_flip(horizontal_flip(matrix))

def rotate_270(matrix):
    return vertical_flip(transpose(matrix))

'''
테스트
'''

def original(m):
    return m

def debug(func, m):
    print(f"===== {func.__name__} =====")
    for row in func(m):
        print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

debug(original, matrix)
debug(rotate_90, matrix)
debug(rotate_180, matrix)
debug(rotate_270, matrix)


'''
응용)

원본 2차원 배열의 일부 영역만을 회전
'''

def rotate_submatrix(matrix, top, left, bottom, right, rotate_func):
    # deep copy
    matrix = [row[:] for row in matrix]

    submatrix = [row[left : right + 1] for row in matrix[top : bottom + 1]]

    rotated_submatrix = rotate_func(submatrix)

    for i, row in enumerate(rotated_submatrix):
        matrix[top + i][left : right + 1] = row

    return matrix

debug(original, rotate_submatrix(matrix, 0, 0, 1, 1, rotate_90))
debug(original, rotate_submatrix(matrix, 0, 0, 1, 1, rotate_180))