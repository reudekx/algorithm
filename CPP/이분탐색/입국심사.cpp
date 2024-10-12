#include <string>
#include <vector>

using namespace std;

long long count(long long total_time, vector<int>& times) {
    long long cnt = 0;
    for (auto& time : times) {
        cnt += total_time / time;
        if (cnt >= 1000000000) break;
    }
    return cnt;
}

long long search(long long s, long long e, int n, vector<int>& times) {
    if (s > e) {
        return s;
    }
    long long mid = (s + e) / 2;
    long long cnt = count(mid, times);
    if (cnt >= n) {
        return search(s, mid - 1, n, times);
    }
    return search(mid + 1, e, n, times);
    
}

long long solution(int n, vector<int> times) {
    long long answer = search(0, 1e18, n, times);
    return answer;
}


/*
풀이 시간: 23분
접근:
    최솟값을 어떻게 구할까..
    
    time의 최솟값이므로, time을 기준으로 매개변수 탐색?
    
    time일 때 각 심사관들이 심사하는 사람 수를 구한다.
    
    만약 time이 큰 경우에는.. 심사한 사람 총 수가 n보다 클 것이다.
        -> 이때는 time을 줄인다.
        
    만약 time이 작은 경우에는.. 심사한 사람 총 수가 n보다 작을 것이다.
        -> 이때는 time을 키운다.
        
    만약 심사한 사람 총 수가 n인 경우에는?
        -> 딱 떨어지지 않을 수 있으므로 time을 줄인다.
        
    즉, n보다 크거나 같으면 left로, n보다 작으면 right로.

시간 복잡도:
    O(심사관 수 * log(최대 시간))
    
    심사관 수 = 10만
    최대 시간은?
        사람이 10억명이고, 각 심사관들이 10억분 걸리면, 10억분 뒤에 심사 끝남.
        따라서 최대 시간은 10억,
        log를 씌우면 30.

후기:
    c++로 코테를 준비하면서 overflow 오류를 처음 겪었다...
    long long 대신 int를 쓰기도 했고, cnt를 구할 때 long long보다 커질 수 있는 것을 생각하지 못했다.
    다만 search 함수에서 상한의 초기값을 10억으로 하면 틀리고 1e18로 했더니 풀렸는데.. 그 이유는 생각을 좀 해봐야겠다.

*/