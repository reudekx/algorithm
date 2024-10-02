def can_process(state):
    n, old_set, new_set, cur, coin, cards = state
    
    new_set.add(cards[cur])
    new_set.add(cards[cur + 1])
        
    for a in old_set:
        for b in old_set:
            if a + b == n + 1:
                old_set.remove(a)
                old_set.remove(b)
                return True, coin
    
    if coin == 0:
        return False, coin
    
    for a in old_set:
        for b in new_set:
            if a + b == n + 1:
                old_set.remove(a)
                new_set.remove(b)
                return True, coin - 1
            
    if coin == 1:
        return False, coin
    
    for a in new_set:
        for b in new_set:
            if a + b == n + 1:
                new_set.remove(a)
                new_set.remove(b)
                return True, coin - 2
    
    return False, coin
    
def solution(coin, cards):
    old_set = set()
    new_set = set()
    n = len(cards)
    for i in range(n // 3):
        old_set.add(cards[i])
    cur = n // 3
    stage = 1
    while cur < n:
        success, coin = can_process([n, old_set, new_set, cur, coin, cards])
        if not success:
            break
        cur += 2
        stage += 1
        
    return stage

'''
풀이 시간: 실패
접근:
    문제 파악)
        최초 덱이 주어진다.
        n/3 장을 뽑아 손패로. 그리고 동전 coin개 존재.
        1. 라운드마다 카드를 2 장 뽑는다. (뽑을 게 없으면 게임 종료)
        2. 뽑은 카드 2개를 각각 1원에 구입하여 가지기 가능
        3. 카드에 적힌 수의 합이 N + 1이 되도록 카드를 내고 다음 라운드로 ㄱㄱ
        
        도달 가능한 최대 라운드 수는?
    유형 파악)
        DP인 것 같은데..
        현재 state = (라운드, 손패, 동전)
        일단 라운드마다 손패는 항상 n / 3장 이하로 시작함. (0 ~ 2장을 추가하고, 2장을 내야 하니까)
        
        state를 최적화 해보자.
        일단 동전은 손패의 수로 구할 수 있지 않을까?
        동전을 소모하지 않으면 패는 n / 3에서 소모하지 않은 만큼 줄어든다.
        
        가령, 동전을 사용하지 않으면 라운드마다 카드가 2장씩 줄어든다.
        
        즉 cur_coin = cur_hand - (n / 3 - round * 2)
        
        따라서 state는 (라운드, 손패)로 충분.
        
        n의 최대 = 166 * 6 = 996
        
        round의 최대 수는? (996 / 3 * 2) / 2 = 332
        
        문제는 손패인데.. 현재 손패의 경우의 수가 너무 많아 보인다.
        
        합을 기준으로 생각해보자.
        라운드 진행을 위해서는 현재 손패의 합에서 n + 1이 되도록 카드를 2장 지불해야 하니까..
        손패의 합에서 n + 1이 줄어든다.
        
        n + 1을 버리는 게 핵심 같은데..
        
        n이 6이라고 가정해보자.
        
        예를 들어 (1, 6) , (2, 5)가 전부 패에 있을 때 각각 중 뭘 버리는지가 중요할까?
        -> 순서는 중요하지 않다.. 즉 버릴 수 있으면 그냥 아무거나 버리면 됨
        
        또한.. 동전을 소모할지 말아야 할지에 대한 기준도 정해져 있는 게 아닌가?
        예를 들어 현재 손패에 3이 있는데 (4, 5)가 등장하면? 4를 무조건 고르는 게 이득이다.
        
        반면.. (2, 3)이 없는데 (4, 5)가 떴다면?? 가져야 할까 버려야할까?
        
        결과적으로 동전의 사용 여부에 따라 경우의 수가 갈리게 된다..
        
        정리해보자.
        
        1. 카드를 구매하여 쌍을 만들 수 있으면 무조건 구매
        2. 또한 n+1을 조합시켜 버리는 건 어떤 카드라도 상관 없음.
        3. 문제는 쌍을 만들 수 없을 때 카드를 구매할지 말지..
        
        항상 최선의 선택
    
        
후기:
    못 풀겠어서 정답을 봤는데..
    뽑은 카드의 구매를 미루고, 나중에 해당 카드가 필요해지면 "사실은 구매했었다"고 간주하여 게임을 진행하면 되는 문제였다..

    최선의 답을 구하기 위해 전지전능한 신이 되었다고 생각한 뒤 문제에 접근해보자

'''