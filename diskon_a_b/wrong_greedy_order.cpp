#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll N, A, B;
    cin >> N >> A >> B;
    vector<ll> arr(N);
    for (auto &x : arr) cin >> x;
    sort(arr.rbegin(), arr.rend());
    ll g = A + B, sisa = N % g, tot = 0;
    for (ll i = 0; i < N; i++){
        if (i < sisa) tot += arr[i];                 // BUG: sisa diambil dari yang termahal
        else if ((i - sisa) % g < A) tot += arr[i];
    }
    cout << tot;
}