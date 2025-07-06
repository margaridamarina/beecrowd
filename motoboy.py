results = []

while True:
    N = int(input())
    if N == 0:
        break

    P = int(input())
    orders = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [0] * (P + 1)           
    for t, p in orders:          
        for c in range(P, p - 1, -1):
            dp[c] = max(dp[c], t + dp[c - p])

    results.append(max(dp))

for r in results:
    print(f"{r} min.")