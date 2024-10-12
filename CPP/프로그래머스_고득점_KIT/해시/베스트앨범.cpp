#include <string>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>


using namespace std;

int sum(vector<pair<int, int>> songs) {
    int total = 0;
    for (auto& song : songs) {
        total += song.second;
    }
    return total;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    map<string, vector<pair<int, int>>> genre_map;
    
    for (int i = 0; i < genres.size(); ++i) {
        genre_map[genres[i]].push_back(make_pair(i, plays[i]));
    }
    
    vector<vector<pair<int, int>>> genre_list;
    
    for (auto& pair : genre_map) {
        genre_list.push_back(pair.second);
    }
    
    sort(genre_list.begin(), genre_list.end(), [](const auto& a, const auto& b) {
        return sum(a) > sum(b);
    });
    
    for (auto& songs : genre_list) {
        sort(songs.begin(), songs.end(), [](const auto& a, const auto& b) {
           return a.first < b.first; 
        });
        
        sort(songs.begin(), songs.end(), [](const auto& a, const auto& b) {
           return a.second > b.second; 
        });
    }
    
    vector<int> answer;
    
    for (auto& songs : genre_list) {
        for (int i = 0; i < min((int)songs.size(), 2); ++i) {
            answer.push_back(songs[i].first);
        }
    }

    return answer;
}

/*
풀이 시간:
접근:
    일단..
        장르별로 plays 리스트를 유지해야 한다.
        이후,
        1. sum(리스트) 내림차순으로 장르를 정렬한다.
        2. 리스트를 고유 번호 오름차순으로 정렬한다.
        3. 리스트를 재생 횟수 내림차순으로 정렬한다. (stable 정렬 이용)
        
        (고유 번호, 재생 횟수) 쌍을 저장해야 한다. pair로
후기:
    점점 c++ 문법에 익숙해져 가고 있고, 단계적으로 침착하게 코드를 작성하니 많은 오류 없이 잘 실행되었다.

*/