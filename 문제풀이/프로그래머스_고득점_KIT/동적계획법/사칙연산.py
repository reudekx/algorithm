INF = 1000 * 101

def calc(start, end, cache, arr):
    if cache[start][end] is not None:
        return cache[start][end]
    if start == end:
        return (int(arr[start]), int(arr[start]))
    max_res = -INF
    min_res = INF
    for i in range(start + 1, end, 2):
        if arr[i] == '+':
            max_res = max(max_res, calc(start, i - 1, cache, arr)[0] + calc(i + 1, end, cache, arr)[0])
            min_res = min(min_res, calc(start, i - 1, cache, arr)[1] + calc(i + 1, end, cache, arr)[1])
        else:
            max_res = max(max_res, calc(start, i - 1, cache, arr)[0] - calc(i + 1, end, cache, arr)[1])
            min_res = min(min_res, calc(start, i - 1, cache, arr)[1] - calc(i + 1, end, cache, arr)[0])
    cache[start][end] = (max_res, min_res)
    return cache[start][end]
        
        

def solution(arr):
    cache = [[None for _ in range(len(arr))] for _ in range(len(arr))]
    
    answer = calc(0, len(arr) - 1, cache, arr)[0]
    return answer



'''
풀이 시간: 56분..
접근:
    DP 카테고리에 있는 문제이므로 DP를 적용하겠지만 모르고 봤으면 스택으로 풀려고 했을 듯?
    일단 시간복잡도부터 확인하자
        숫자 -> 최대 101개
        연산자 -> 최대 100개
        
        100개의 연산자의 연산 순서를 정해줘야 함. ->100!
        
        가령 50개의 연산자를 나열한 뒤 나머지 50개를 확인할 때
        이전 연산자들의 순서가 중요한가? -> 아니다
        덧셈과 뺄셈만으로 이루어져 있으므로 앞 표현식의 결과를 최대한 크게 유지하면 된다.
        
        따라서 연산자의 사용 여부만 중요함.
        -> 그래도 2^100인 것 같은데..
        
    선형적으로 접근할 필요가 있다..
        연산자가 다음 숫자에 즉시 apply되거나,
        아니면 right 표현식 전체에 apply 되거나..
        
        다만 다음과 같은 표현식을 처리 가능한지?
        
        1 - (2 + 3 + 4) - 5
        
        즉 중간에 끊어주는 게 가능할까?
        -> 안 되는 것 같은데..
        scope가 열렸다가 다시 닫히려면.. 맥락을 유지해야할 것 같은데
        
    다시 생각해보자..
        결과적으로 표현식을 파싱하면 이진 트리가 등장한다.
        최초의 연산자를 선택하여 left와 right로 나눠주면 된다.
        
        연산자가 +인 경우:
            left와 right가 최대가 되면 된다.
        연산자가 -인 경우:
            left는 최대, right는 최소가 되어야 한다.
            
        이 경우, 각 구간에 대해 최대값과 최소값을 알 필요가 있다.
            -> 따로 저장해야 함.
후기:
    풀이를 떠올리는 게 굉장히 힘들었다..
    정답의 최종 형태가 어떻게 나타날지를 잘 생각해야겠다.
    이 문제의 경우.. 소괄호를 어디에 치든 상관없이 항상 이진 트리 꼴로 정답을 표현할 수 있다는 것을 떠올려야 했다.
'''