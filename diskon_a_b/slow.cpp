#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll N, A, B;
    cin >> N >> A >> B;
    vector<ll> arr(N);
    for (auto &x : arr) cin >> x;
    ll g = A + B, sisa = N % g, tot = 0;
    vector<bool> used(N, false);
    for (ll i = 0; i < N; i++){                      // ambil maksimum satu per satu: O(N^2)
        ll best = -1;
        for (ll j = 0; j < N; j++)
            if (!used[j] && (best == -1 || arr[j] > arr[best])) best = j;
        used[best] = true;
        if (i < N - sisa){ if (i % g < A) tot += arr[best]; }
        else tot += arr[best];
    }
    cout << tot;
}