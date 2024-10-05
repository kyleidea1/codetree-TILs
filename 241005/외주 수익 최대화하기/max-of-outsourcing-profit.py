def max_profit(n, jobs):
    jobs.sort(key=lambda x: x[0])
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i-1]

        for t, p in jobs:
            if i == t:
                dp[i] = max(dp[i], dp[i-t] + p)
    
    return dp[n]

n = int(input())
jobs = []
for _ in range(n):
    t, p = map(int, input().split())
    jobs.append((t, p))

print(max_profit(n, jobs))