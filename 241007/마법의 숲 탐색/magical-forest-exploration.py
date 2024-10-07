from collections import deque
import sys
input = sys.stdin.readline

def get_golem_pos(center):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        x,y = center
        nx += dx[i]
        ny += dy[i]
        pos.append((nx,ny))
return pos

def go_down(golem):
    for d in golem:
        d[1] -= 1
    return golem

print(get_golem_pos(2,3))