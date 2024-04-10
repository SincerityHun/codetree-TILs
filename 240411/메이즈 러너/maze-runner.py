# N*N
# 미로의 한칸 -> 빈칸, 벽, 출구
# 빈칸 : 참가자 이동 가능
# 벽: 이동X, 1~9의 내구도, 회전할 때 1 깍임, 0되면 빈칸으로 변경
# 출구: 해당 칸에 참가자 도달 -> 즉 탈

# 1초마다 한칸 이동
# 최단거리 행차이 열차이 더한거
# 동시에 움직임
# 현재보다 더 가까운 경로로만 움직임
# 더 가까워지지 않으면 안 움직이고
# 더 가까워지는 선택이 여러개라면 -> 상 하를 우선시 여김
# 한칸에 2명 이상의 참가자 있을 수 있음

# 이동 끝났으면 미로 회전
# 한명 이상의 참가자 + 출구를 포함 가장 작은 정사각형
# 2개 이상이라면 좌상단 기준 R좌표가 작은 것이 우선, c좌표가 작은 것이 우선
# 시계방향 90도 회전 + 회전된 애들은 내구도 1씩 깍임

# K초 동안 과정 반복 -> 전에 탈출? 바로 끝남
# 게임이 끝났을 ㄸ, 모든 참가자들의 이동거리 합과 출구 좌표를 출력
import sys
row_num, user_num, time_limit = map(int, sys.stdin.readline().rstrip().split())

# 미로 형태 받기
matrix = []
for i in range(row_num):
    matrix.append(list(map(int,sys.stdin.readline().rstrip().split())))

# 유저 받기
user_matrix = [[set() for x in range(row_num)]for _ in range(row_num)]

user_dict = dict()
user_exit = [False]*user_num
user_move = [0]*user_num
dr = [-1,1,0,0] # 상,하,좌,우
dc = [0,0,-1,1]

for i in range(user_num):
    r,c = map(int, sys.stdin.readline().rstrip().split())
    r -= 1
    c -= 1
    user_dict[i] =(r,c)
    user_matrix[r][c].add(i)

# 출구 받기
exit_index = tuple(map(int, sys.stdin.readline().rstrip().split()))
exit_index = (exit_index[0]-1,exit_index[1]-1)
# 범위 확인
def in_range(r,c):
    return 0<=r<row_num and 0<=c<row_num and matrix[r][c] == 0

# 정사각형 안에 사람이 적어도 하나씩 있는 지 확인
def check_people_in(check_r,check_c,turn_maze_row):
    if not(0<=check_r<row_num and 0<=check_c<row_num):
        return False
    if not(0<=(check_r + turn_maze_row -1)<row_num and 0<=(check_c + turn_maze_row -1)<row_num):
        return False
    for i in range(check_r,check_r + turn_maze_row):
        for j in range(check_c, check_c + turn_maze_row):
            if len(user_matrix[i][j]) != 0:
                return True
    return False

# 정사각형 회전
def turn_matrix(start_r,start_c,turn_maze_row):
    global exit_index
    temp_matrix = [[0]*turn_maze_row for _ in range(turn_maze_row)]
    for i in range(start_r,start_r + turn_maze_row):
        for j in range(start_c,start_c + turn_maze_row):
            if matrix[i][j] != 0:
                temp_matrix[j - start_c][turn_maze_row - 1 - i + start_r] = matrix[i][j] - 1
            elif (i,j) == exit_index:
                temp_matrix[j - start_c][turn_maze_row - 1 - i + start_r] = -1
    for i in range(start_r,start_r + turn_maze_row):
        for j in range(start_c,start_c + turn_maze_row):
            matrix[i][j] = temp_matrix[i-start_r][j-start_c]
            if matrix[i][j] == -1:
                exit_index = (i,j)
                matrix[i][j] = 0

# 유저 동기화
def turn_user_matrix(start_r,start_c,turn_maze_row):
    temp_matrix = [[set() for x in range(turn_maze_row)] for _ in range(turn_maze_row)]
    for i in range(start_r, start_r + turn_maze_row):
        for j in range(start_c, start_c + turn_maze_row):
            if len(user_matrix[i][j]) != 0:
                temp_matrix[j - start_c][turn_maze_row - 1 - i + start_r].update(user_matrix[i][j])

    for i in range(start_r, start_r + turn_maze_row):
        for j in range(start_c, start_c + turn_maze_row):
            user_ID = temp_matrix[i - start_r][j - start_c]
            user_matrix[i][j].clear()
            user_matrix[i][j].update(user_ID)
            if len(user_ID) != 0:
                for id in user_ID:
                    user_dict[id] = (i,j)
# 타이머 시작
for _ in range(time_limit):
    # 참가자 이동
    for i in range(user_num): 
        if user_exit[i]:
            continue
        # 2. 현재 거리 계산
        cur_r,cur_c = user_dict[i]
        exit_r,exit_c = exit_index
        cur_distance =  abs(cur_r - exit_r) + abs(cur_c - exit_c)
        cur_dir = -1
        # 3. for 0~3 까지해서 각 방향의 거리 확인 + 현재 거리와 비교해서 더 작으면 업데이트
        for j in range(4):
            next_r,next_c = cur_r+dr[j],cur_c+dc[j]
            if not in_range(next_r,next_c):
                continue
            next_distance = abs(next_r - exit_r) + abs(next_c - exit_c)
            if (next_distance,j) < (cur_distance,cur_dir):
                cur_distance = next_distance
                cur_dir = j
        # 4. flag가 true가 아니면 나가 너 이동못해
        if cur_dir == -1:
            continue
        # 5. 실제 이동 -> 동기화(user_matrix,user_dict,user_move)
        user_matrix[cur_r][cur_c].remove(i)
        next_r, next_c = cur_r + dr[cur_dir], cur_c + dc[cur_dir]
        user_matrix[next_r][next_c].add(i)
        user_dict[i] = (next_r,next_c)
        user_move[i] += 1
        # 6. 이동 후 위치 확인 -> 동기화(user_exit)
        if user_dict[i] == exit_index:
            user_exit[i] = True
            user_matrix[user_dict[i][0]][user_dict[i][1]].remove(i)
    # 미로 회전
    for turn_maze_row in range(2,row_num+1):
        # 1. 현재 탈출구 찾기
        exit_r,exit_c = exit_index
        # 2. 정사각형 탐색
        flag = False
        start_r,start_c = (0,0)
        for check_r in range(exit_r - turn_maze_row + 1,exit_r + 1):
            for check_c in range(exit_c - turn_maze_row + 1, exit_c + 1):
                if check_people_in(check_r,check_c,turn_maze_row):
                    flag = True
                    start_r,start_c = check_r,check_c
                    break
            if flag:
                break
        if not flag:
            continue
        # 3. maze 90도 회전 -> 내구도 1씩 깍기, exit 90도 회전
        turn_matrix(start_r,start_c,turn_maze_row)
        # 4. user_matirx 90도 회전 -> user_dict 동기화
        turn_user_matrix(start_r,start_c,turn_maze_row)


        break

score = 0
for i in range(user_num):
    score += user_move[i]
print(score)
print(exit_index[0]+1,exit_index[1]+1)