#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string, int> sub;

    for (auto& p : participant) {
        sub[p]++;
    }
    
    for (auto& c : completion) {
        sub[c]--;
    }
    
    string answer;
    
    for (auto& s : sub) {
        if (s.second == 1) {
            answer = s.first;
            break;
        }
    }
    
    return answer;
}


/*
풀이 시간: 5분 30초
접근:
    participant에는 있는데 completion에는 없는 선수
    
    동명이인 처리는?
후기:
    문법에 익숙해져가는 중이다.
*/