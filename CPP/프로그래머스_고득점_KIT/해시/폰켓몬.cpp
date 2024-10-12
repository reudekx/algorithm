#include <vector>
#include <set>

using namespace std;

int solution(vector<int> nums)
{
    set<int> kind;
    
    for (auto& mon : nums) {
        kind.insert(mon);
    }
    
    int answer = kind.size() < nums.size() / 2 ? kind.size() : nums.size() / 2;
    return answer;
}

/*
풀이 시간: 3분 30초
접근:
    N / 2 마리를 가져간다..
    
    min(각 폰켓몬의 종류, N / 2)를 반환.
후기:
    C++에 익숙지 않아 조금 시간이 걸렸다. 여러 문제들을 풀어보자..
*/