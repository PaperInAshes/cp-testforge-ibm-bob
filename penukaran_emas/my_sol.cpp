#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> dp(N+1,0);
    dp[0]=0;
    for (int i = 0; i <= N; i++){
        int pil1 = i;
        int pil2 = dp[i/2] + dp[i/3] + dp[i/4];
        dp[i]=max(pil1,pil2);
    }
    cout << dp[N];
}