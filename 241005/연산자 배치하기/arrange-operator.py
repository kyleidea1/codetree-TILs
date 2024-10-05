from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
q = deque([(numbers[0], op, 1)]) # 처리한 개수도 추가

def bfs(q,op,numbers):
    ans = []
    while q:
        cur, op, idx = q.popleft()
        if idx == n:
            ans.append(cur)
            continue
        else:
            new = numbers[idx]
            for i in range(3):
                if op[i] > 0:
                    new_op = op[:] # 개중요
                    new_op[i] -= 1
                    if i == 0:
                        q.append((cur + new, new_op, idx + 1))
                    elif i == 1:
                        q.append((cur - new, new_op, idx + 1))
                    else:
                        q.append((cur * new, new_op, idx + 1))
    return ans

ans = bfs(q,op,numbers)
print(min(ans),max(ans))