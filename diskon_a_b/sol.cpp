#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, A, B;
    cin >> N >> A >> B;
    vector<ll>arr(N);

    if (N < A + B){
        ll tot = 0;
        for (int i = 0; i < N; i++){
            ll temp;
            cin >> temp;
            tot += temp;
        }
        cout << tot;
    }else{
        for (int i = 0; i < N; i++){
            cin >> arr[i];
        }
        sort(arr.rbegin(), arr.rend());
        int A1 = A, B1 = B, sisa = N % (A+B), N1 = N;
        ll tot = 0;
        for (int i = 0; i < N; i++){
            if (N1 > sisa){
                if (A1 == 0 && B1 == 0){
                    A1 = A;
                    B1 = B;
                }
                if (A1 != 0){
                    tot += arr[i];
                    A1--;
                }else if(A1 == 0 && B1 != 0){
                    B1--;
                }
            }else{
                tot += arr[i];
            }
            N1--;
        }
        cout << tot;
    }
}