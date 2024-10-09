#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer = {arr[0]};

    for (int i = 1; i < arr.size(); ++i) {
        if (arr[i] == answer.back()) continue;
        answer.push_back(arr[i]);
    }

    return answer;
}

/*

후기:
    back()을 통해 마지막 원소를 참조할 수 있다.

*/