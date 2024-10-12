#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    map<string, int> cnt;
    
    for (auto& cloth : clothes) {
        cnt[cloth[1]]++;
    }
    
    int answer = 1;
    
    for (auto& pair : cnt) {
        answer *= pair.second + 1;
    }
    
    answer--;
    
    return answer;
}

/*
풀이 시간: 5분 20초
접근:
    옷의 종류별 개수를 센다.
    
    그리고 각 개수를 곱한 뒤 1을 빼준다. (옷을 안 입은 경우를 빼준다.)

후기:
    문법에 익숙해지는 중..

*/