def can_accurate(player, n, win, lose):
    visited = [False for _ in range(n + 1)]
    
    def dfs(cur, graph):
        visited[cur] = True
        cnt = 1
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            cnt += dfs(nxt, graph)
        return cnt
    
    win_cnt = dfs(player, win) - 1
    lose_cnt = dfs(player, lose) - 1
    
    return win_cnt + lose_cnt == n - 1

def count(n, win, lose):
    cnt = 0
    for i in range(1, n + 1):
        cnt += int(can_accurate(i, n, win, lose))
    return cnt

def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)
    
    answer = count(n, win, lose)
    return answer

'''
풀이 시간: 13분
접근:
    정확한 순위는 어떻게 구해질까?
    재귀적으로 구할 수 있다고 하더라고, base case는 어떻게 설정하지?
    
    자신을 이긴 선수의 수와 자신에게 진 선수의 수의 합이 n - 1이라면 순위가 결정된다.
    그 과정에서 재귀적 연산을 이용.
후기:
    다른 사람의 풀이)
        from collections import defaultdict

        # 기본값이 빈 set가 됨.
        win, lose = defaultdict(set), defaultdict(set) 

        이후 results 리스트를 순회하며 win[a].add(b), lose[b].add(a)를 해주고

        for i in range(1, n + 1):
            for winner in lose[i]:
                win[winner].update(win[i])
            for loser in win[i]:
                lose[loser].update(lose[i])

        위 방법으로 set를 update 해준 뒤 개수를 검사해주면 됨.

    
'''