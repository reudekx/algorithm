#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

const int MAX_NODES = 11;

vector<char> name = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
};
int cnt = name.size();

bool connected[MAX_NODES][MAX_NODES] = {
    {false, true,  false, true,  true,  false, false, false, false, false, false},
    {true,  false, true,  true,  false, false, false, false, false, false, false},
    {false, true,  false, false, false, true,  true,  false, false, false, false},
    {true,  true,  false, false, true,  false, false, true,  false, false, false},
    {true,  false, false, true,  false, false, false, true,  true,  false, false},
    {false, false, true,  false, false, false, true,  false, false, true,  false},
    {false, false, true,  false, false, true,  false, false, false, true,  true },
    {false, false, false, true,  true,  false, false, false, true,  false, true },
    {false, false, false, false, true,  false, false, true,  false, false, true },
    {false, false, false, false, false, true,  true,  false, false, false, true },
    {false, false, false, false, false, false, true,  true,  true,  true,  false}
};

vector<bool> visited(MAX_NODES);

void print_graph() {
    cout << "   ";
    for (char c : name) {
        cout << c << " ";
    }
    cout << '\n';

    for (int i = 0; i < cnt; ++i) {
        cout << name[i] << ": ";
        for (int j = 0; j < cnt; ++j) {
            cout << (connected[i][j] ? "1" : "0");
        }
        cout << '\n';
    }
}

void dfs(int cur) {
    cout << name[cur] << " ";
    visited[cur] = true;
    for (int nxt = 0; nxt < cnt; ++nxt) {
        if (!connected[cur][nxt] || visited[nxt]) continue;
        dfs(nxt);
    }
}

void bfs(int cur) {
    queue<int> q;
    q.push(cur);
    visited[cur] = true;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        cout << name[cur] << " ";

        for (int nxt = 0; nxt < cnt; ++nxt) {
            if (!connected[cur][nxt] || visited[nxt]) continue;
            visited[nxt] = true;
            q.push(nxt);
        }
    }
}

void search(void (*func)(int), int start, const string& func_name) {
    for (int i = 0; i < cnt; ++i) {
        visited[i] = false;
    }

    func(start);
}

int main() {
    print_graph();

    search(dfs, 0, "dfs");

    cout << "\n";

    search(bfs, 0, "bfs");

    return 0;
}