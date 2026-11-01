#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, A, B;
    cin >> N >> A >> B;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];
    sort(arr.rbegin(), arr.rend());
    int tot = 0;                       // BUG: harusnya long long
    int g = A + B;
    for (int i = 0; i < N; i++){
        if (i / g < N / g){            // barang yang masuk kelompok penuh
            if (i % g < A) tot += arr[i];
        } else tot += arr[i];
    }
    cout << tot;
}