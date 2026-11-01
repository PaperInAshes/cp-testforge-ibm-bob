n, x = map(int, input().split())
coins = sorted(map(int, input().split()), reverse=True)
count = 0
for c in coins:
    count += x // c
    x %= c
print(count if x == 0 else -1)