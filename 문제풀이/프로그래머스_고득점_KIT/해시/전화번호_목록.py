
def solution(phone_book):
    tree = {}
    for phone_num in phone_book:
        cur = tree
        is_prefix = True
        for num in phone_num:
            if num not in cur:
                cur[num] = {}
                is_prefix = False
            else:
                if len(cur[num]) == 0:
                    return False
            cur = cur[num]
        if is_prefix:
            return False

    return True

'''
풀이 시간: 19분
접근:
    시간 복잡도 때문에 2중 for문 검사는 불가능하다.
    선형적으로 검사해야 함.
후기:
    생각보다 까다로웠다..

    또한 접두사가 될 수 있는 전화번호가 먼저 사전에 들어가는 경우를 체크 했어야 했다.

'''