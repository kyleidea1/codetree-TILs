import sys
input = sys.stdin.readline

n = int(input())
jobs = []
for _ in range(n):
    jobs.append(tuple(map(int,input().split())))

jobs.sort(lambda x: x[0])
dp = [0]*(n+1)

for i in range(1,n+1):
    for t,p in jobs:
        dp[i] = max(dp[i-1], dp[i-t]+p)

print(max(dp))