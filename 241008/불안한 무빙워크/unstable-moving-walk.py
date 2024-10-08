import sys
from collections import deque

n, k = map(int,input().split())
safety = deque(list(map(int,input().split())))
moving_walk = deque([i for i in range(1,2*n+1)])
ppl = deque([])
zero_cnt = 0

def simulation():
    global zero_cnt
    moving_walk.appendleft(moving_walk.pop())
    safety.appendleft(safety.pop())

    for i in range(len(ppl)):
        if ppl[i] < n-1 and ppl[i]+1 not in ppl:
            ppl[i] += 1
            safety[ppl[i]] -= 1
            if safety[ppl[i]] == 0:
                zero_cnt += 1
            if ppl[i] == n-1:
                ppl.pop()

    if 0 not in ppl and safety[0]:
        ppl.appendleft(0)
        safety[0] -= 1
        if safety[0] == 0:
            zero_cnt += 1

cnt = 0
while zero_cnt < k:
    simulation()
    cnt += 1
print(cnt+1)