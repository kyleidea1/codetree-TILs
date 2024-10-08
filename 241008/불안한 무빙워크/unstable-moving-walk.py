from collections import deque

def move_people():
    global zero_cnt
    moved_people = deque()
    
    while ppl:
        pos = ppl.popleft()
        if pos == n - 1:  # n번 칸에 도달한 경우 (0-based index)
            continue
        
        next_pos = pos + 1
        if next_pos not in ppl and safety[next_pos] > 0:
            safety[next_pos] -= 1
            if safety[next_pos] == 0:
                zero_cnt += 1
            moved_people.append(next_pos)
        else:
            moved_people.append(pos)
    
    ppl.extend(moved_people)

def simulation():
    global zero_cnt
    
    # 1. 무빙워크 회전
    safety.rotate(1)
    
    # 사람들의 위치도 회전에 맞춰 조정
    for i in range(len(ppl)):
        ppl[i] = (ppl[i] + 1) % (2*n)
    
    # n번 칸에 도달한 사람 제거
    while ppl and ppl[0] == n - 1:
        ppl.popleft()
    
    # 2. 사람 이동
    move_people()
    
    # 3. 새 사람 탑승
    if not ppl or ppl[0] != 0:  # 첫 번째 칸에 사람이 없다면
        if safety[0] > 0:
            safety[0] -= 1
            if safety[0] == 0:
                zero_cnt += 1
            ppl.appendleft(0)

n, k = map(int, input().split())
safety = deque(list(map(int, input().split())))
ppl = deque()
zero_cnt = 0

cnt = 0
while zero_cnt < k:
    simulation()
    cnt += 1

print(cnt)