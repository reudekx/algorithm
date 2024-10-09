#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    int open_cnt = 0;
    
    for (auto& ch : s) {
        open_cnt += ch == '(' ? 1 : -1;
        if (open_cnt < 0) break;
    }
    
    return open_cnt == 0;
}

/*
풀이 시간: 3분
접근:
후기:
    간단한 문제였다..

*/