n, x = map(int, input().split())
coins = list(map(int, input().split()))
INF = float('inf')
dp = [0] + [INF] * x
for i in range(1, x + 1):
    for c in coins:
        if c <= i and dp[i - c] + 1 < dp[i]:
            dp[i] = dp[i - c] + 1
print(dp[x] if dp[x] != INF else -1)