#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll N, A, B;
    cin >> N >> A >> B;
    vector<ll> arr(N);
    for (auto &x : arr) cin >> x;
    sort(arr.rbegin(), arr.rend());
    ll tot = 0, g = A + B;
    if (N <= g){                       // BUG: harusnya N < g
        for (ll x : arr) tot += x;
    } else {
        for (ll i = 0; i < N; i++){
            if (i / g < N / g){
                if (i % g < A) tot += arr[i];
            } else tot += arr[i];
        }
    }
    cout << tot;
}