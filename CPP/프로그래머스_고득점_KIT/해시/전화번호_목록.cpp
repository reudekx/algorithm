#include <string>
#include <vector>
#include <map>

using namespace std;

using Node = map<int, void*>;

bool check_prefix(vector<string>& phone_book) {
    Node* tree = new Node;
    for (auto& phone_num : phone_book) {
        Node* cur = tree;
        bool is_prefix = true; // 현재 phone_num이 prefix인지
        for (auto& num : phone_num) {
            if (cur->find(num) == cur->end()) { // 원소가 없는 경우
                (*cur)[num] = new Node;
                is_prefix = false;
            }
            else {
                if (((Node *)(*cur)[num])->size() == 0) return true; // 현재 phone_num의 접두사를 찾은 경우
            }
            cur = (Node*)(*cur)[num];
        }
        if (is_prefix) return true;
    }
    return false;
}


bool solution(vector<string> phone_book) {
    bool answer = !check_prefix(phone_book);
    return answer;
}

/*
풀이 시간: 25분
접근:
    정렬을 하지 않고 map을 이용해 풀어보자.
    재귀적 구조를 만들 수 있을까?
후기:
    파이썬으로 이미 풀어본 문제임에도 불구하고 방법을 까먹어서 다시 생각하는데 조금 걸렸고..
    is_prefix 변수의 역할에 대해 중간에 혼동이 왔었다. -> 주석을 잘 달자.

    그리고 포인터 캐스팅 과정에서.. 괄호를 한 쌍 빼먹어서 오류가 났었다. 
    -> 뭔가 해결이 잘 안 되었었는데, 해당 부분의 코드를 지우고 다시 작성했더니 해결됐다.
*/