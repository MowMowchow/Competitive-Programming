#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <queue>
#define MAXN 100001
using namespace std;


int N, M, x, y, w;
vector<int> roads[MAXN];
vector<int> times[MAXN];
int available1[MAXN], available2[MAXN];


int main() {
    cin >> N >> M;
    for (int i = 0; i < M; i++){
        cin >> x >> y >> w;
        roads[x].push_back(y);
        roads[y].push_back(x);
        times[x].push_back(w);
        times[y].push_back(w);
    }

    //spfa 1
    fill_n(available1, MAXN, 999999);
    available1[0] = 0;
    queue<vector<int > > cityqueue1;
    queue<int> timequeue1;

    for (int i = 0; i < roads[0].size(); i++){
        vector<int> temp; temp.push_back(0); temp.push_back(roads[0][i]);
        cityqueue1.push(temp);
        timequeue1.push(times[0][i]);
    }

    while (!cityqueue1.empty()){
        vector<int> temp = cityqueue1.front(); cityqueue1.pop();
        int x = temp[0], y = temp[1];
        int time = timequeue1.front(); timequeue1.pop();

        if (available1[x] + time < available1[y]){
            available1[y] = available1[x] + time;

            for (int city = 0; city < roads[y].size(); city++){
                vector<int> temp = {y, roads[y][city]};
                cityqueue1.push(temp);
                timequeue1.push(times[y][city]);
            }
        }
    }

    // spfa 2
    fill_n(available2, MAXN, 999999);
    available2[N-1] = 0;
    queue<vector<int > > cityqueue2;
    queue<int> timequeue2;

    for (int i = 0; i < roads[N-1].size(); i++){
        vector<int> temp; temp.push_back(N-1); temp.push_back(roads[N-1][i]);
        cityqueue2.push(temp);
        timequeue2.push(times[N-1][i]);
    }

    while (!cityqueue2.empty()){
        vector<int> temp = cityqueue2.front(); cityqueue2.pop();
        int x = temp[0], y = temp[1];
        int time = timequeue2.front(); timequeue2.pop();

        if (available2[x] + time < available2[y]){
            available2[y] = available2[x] + time;

            for (int city = 0; city < roads[y].size(); city++){
                vector<int> temp = {y, roads[y][city]};
                cityqueue2.push(temp);
                timequeue2.push(times[y][city]);
            }
        }
    }

    int maxdist = 0;
    for (int i = 0; i < N; i++){
        maxdist = max(maxdist, available1[i]+available2[i]);
    }
    cout << maxdist;
    return 0;
}