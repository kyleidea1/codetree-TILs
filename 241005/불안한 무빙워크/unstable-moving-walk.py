from collections import deque

n,k = map(int,input().split())
l = list(map(int,input().split()))
up = deque(l[:n])
down = deque(l[n:][::-1])
pos = deque([])
cnt = 0
zero_cnt = 0

def rotate(pos,up,down):
    new_pos = deque([i+1 for i in list(pos)]) # 한 칸 이동시키고
    if n-1 in new_pos: # n에 사람 도달 시 즉시 내림
        pos.pop()
    up.appendleft(down.popleft())
    down.append(up.pop())
    return new_pos,up,down

def move(zero_cnt,pos,up,down): #pos:deque
    new_pos = deque([])
    while pos:
        cur = pos.pop()
        if cur+1 == n-1: #n에 도달하면 즉시 내림
            up[n-1] -= 1
            if up[cur+1] == 0:
                zero_cnt += 1
        elif cur+1 < n-1 and up[cur+1] != 0:
            if cur+1 not in pos:
                new_pos.append(cur+1)
                up[cur+1] -= 1
                if up[cur+1] == 0:
                    zero_cnt += 1
            else:
                new_pos.append(cur)
    return zero_cnt,new_pos,up,down

def put(pos,up,down):
    pos.appendleft(0)
    return pos,up,down

while zero_cnt < k:
    pos,up,down = rotate(pos,up,down)
    zero_cnt,pos,up,down = move(zero_cnt,pos,up,down)
    if 0 not in pos and up[0] != 0:
        pos.appendleft(0)
        up[0] -= 1
        if up[0] == 0:
            zero_cnt += 1
    cnt += 1

print(cnt)