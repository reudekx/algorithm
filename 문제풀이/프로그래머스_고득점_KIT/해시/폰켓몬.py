from collections import defaultdict

def solution(nums):
    mon = defaultdict(int)
    for num in nums:
        mon[num] += 1
    return len(mon) if len(mon) < len(nums) // 2 else len(nums) // 2

'''
풀이 시간: 3분
접근:
후기:
    레벨 1 문제

    dict대신 set로 푸는 게 적절한 것 같다..

'''