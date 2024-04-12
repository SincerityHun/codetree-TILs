# n*n 격자판
# 1*1 사이즈 정육면체
# 굴릴거임
# 1~6까지 써있고 m번에 걸쳐서 1칸씩 굴릴거임
# 마주보는 면의 숫자 합은 7
# 항상 (0,0)에서 출발
# 처음에는 오른쪽으로 이동
# 주사위가 놓인 칸과 상하좌우 인접하며 같은 숫자인 칸의 합
# 숫자 계싼하고 아랫면이 보드의 해당칸에 있는 숫자보다 크면 -> 현재 진행방향 90도로 ㄱ
# 작다면 현재 진행방향 90도 반시계
# 같다면 현재 방향 ㄱ
from collections import deque
row_num, turn_num = map(int,input().split())
matrix = []
for _ in range(row_num):
    matrix.append(list(map(int,input().split())))
# 우,하,좌,상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
box_info = (0,0,0) # 주사위 현재 r, 주사위 현재 c, 주사위 현재 dir
turn_left_right = deque([6,3,1,4])
turn_high_low = (5,2)

def in_range(r,c):
    return (0<=r<row_num) and (0<=c<row_num)
# Simulation
score = 0
for i in range(turn_num):
    box_r,box_c,box_dir = box_info
    # 1. box info dir 방향대로 움직임(나갈 경우, dir 변경) -> box info의 r,c 업데이트
    next_r,next_c = box_r+dr[box_dir],box_c+dc[box_dir]
    if not in_range(next_r,next_c):
        box_dir = (box_dir+2)%4
        next_r, next_c = box_r + dr[box_dir], box_c + dc[box_dir]
    # 2. box info  dir에 따라 turn_left_right, turn_high_low 업데이트
    if box_dir == 0:
        turn_left_right.append(turn_left_right.popleft())
    elif box_dir == 1:
        temp = (turn_left_right[0],turn_left_right[2])
        turn_left_right[2],turn_left_right[0] = turn_high_low
        turn_high_low = temp
    elif box_dir == 2:
        turn_left_right.appendleft(turn_left_right.pop())
    elif box_dir == 3: # 상
        temp = (turn_left_right[2], turn_left_right[0])
        turn_left_right[0],turn_left_right[2] = turn_high_low
        turn_high_low = temp
    # 3. 격자 숫자 조회하고 BFS 돌려서 몇개 있는지 확인 -> Score 업데이트
    criteria = matrix[next_r][next_c]
    visited = set()
    visited.add((next_r,next_c))
    bfs_queue = deque([(next_r,next_c)])
    count = 1
    while len(bfs_queue) != 0:
        cur_r,cur_c = bfs_queue.popleft()
        for i in range(4):
            n_r,n_c = cur_r+dr[i],cur_c+dc[i]
            if in_range(n_r,n_c) and (n_r,n_c) not in visited:
                visited.add((n_r,n_c))
                if matrix[n_r][n_c] == criteria:
                    bfs_queue.append((n_r,n_c))
                    count += 1
    score += (count*criteria)
    # 4. 격자 숫자랑 맨 밑면 숫자 비교해서 다음 dir 정해주기
    base_num = turn_left_right[0]
    if criteria > base_num:
        box_dir = (box_dir-1) % 4
    elif criteria < base_num:
        box_dir = (box_dir+1) % 4
        # 격자 숫자 > 맨 밑면 -> 90도 반시계방향 업데이트
        # 격자 숫자 == 맨 밑면 -> 그대로
        # 격자 숫자 < 맨 밑면 -> 90e도 시계 방향dir 업데이트
    # 5. 업데이트
    box_info = (next_r,next_c,box_dir)

print(score)