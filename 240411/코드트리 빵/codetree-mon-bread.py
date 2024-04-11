# m명의 사람 빵구하러함
# 1번 ->1분, 2번 -> 2분,,,,m번 사람은 정확히 m분에 각자의 베이스캠프에서 출발->편의점
# 출발 전에는 격자밖
# 목표로 하는 편의점 모두 다름
# n*n 사이즈 격자

# 3가지 행동 1분
# 1 2 3순서
# 1.
# 격자에 있는 모든 사람 본인이 가고 싶은 편의점 방향을 향해서 1칸
# 최단거리, 여러개라면 상 좌 우 하,
# 여기서 최단거리 => 이동 가능한 칸으로만 이동해 도달하기까지 거쳐야 하는 칸의 수가 최소
# 2.
# 만약에 편의점 도착 -> 해당 편의점에서 멈춤
# 누가 거기 멈춰있으면 지나갈 수가 없음
# 3. 베이스캠프로 ㅅ환
# 현재 시간 t분, 근데 t<=m이라면,  1번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스캠프
# 최단 거리에 있는 베이스캠프
# 이때, 베이스캠프가 여러개 -> 행이작고, 그거 마저 같다면 열이 작은
# 이때, t번 사람이 베이스 캠프로 가는건 시간이 소요 안됨
# 다른 사람들은 그 칸을 지나갈 수 없음
# 또한, 1번 베이스캠프에서 소환된 1번 유저가 필드에 있으면 1번 베이스캠프에는 아무도 못온다.
# 포인트: 모두 이동이 끝나고, 편의점 + 베이스캠프를 이동 못하게 막는 것
# 총 몇분 걸려 모두 편의점에 도착하나요?
from collections import deque
row_num, user_num = map(int,input().split())

# Basecamp 정보 받기
# 0->빈칸, 1-> 베이스캠프, 2-> 이동 불가
matrix = []
for _ in range(row_num):
    matrix.append(list(map(int,input().split())))

# 유저 정보 받기
user_destination = dict()
user_current_position = dict()
user_start = [False] * (user_num+1)
user_goal = [False] * (user_num+1)
dr = [-1,0,0,1]
dc = [0,-1,1,0]
for id in range(1,user_num+1):
    r,c= tuple(map(int,input().split()))
    user_destination[id] = (r-1,c-1)

# 시뮬레이션
time = 0
# 겜 끝났는 지 확인하는 함수
def end_game():
    for id in range(1,user_num+1):
        if not user_goal[id]:
            return False
    return True

def in_range(r,c):
    return (0<=r<row_num) and (0<=c<row_num) and matrix[r][c] != 2
def update_matrix():
    # 이미 출발한 사람들 대상으로 하기
    for user_ID in range(1,user_num+1):
        if not user_start[user_ID]:
            continue
        if user_goal[user_ID]:
            continue
    # 현재 위치 받기 user_current_position 조회
        cur_r,cur_c = user_current_position[user_ID]
    # 목표로 하는 위치 받기 user_destination 조회
        dest_r,dest_c = user_destination[user_ID]
    # bfs + 경로 저장 사용해서 최단 거리 구하기
        bfs_queue = deque([(cur_r,cur_c)])
        prev_node = {(cur_r,cur_c):None}
        while len(bfs_queue) != 0:
            temp_r,temp_c = bfs_queue.popleft()
            if (temp_r,temp_c) == (dest_r,dest_c):
                break
            for dir in range(4):
                next_r,next_c = temp_r+dr[dir],temp_c+dc[dir]
                if in_range(next_r,next_c) and (next_r,next_c) not in prev_node:
                    prev_node[(next_r,next_c)] = (temp_r,temp_c)
                    bfs_queue.append((next_r,next_c))
    # prev타고 뒤로 돌아와서 prev가 현재 위치인 노드 찾기
        if (dest_r,dest_c) in prev_node:
            pointer = (dest_r,dest_c)
            while prev_node[pointer] != (cur_r,cur_c):
                pointer = prev_node[pointer]
    # 해당 노드로 user_current_position 업데이트
            user_current_position[user_ID] = pointer
def check_destination():
    # 이미 출발했고, 아직 도착안한 사람들 대상으로 하기
    for user_ID in range(1,user_num+1):
        if (not user_start[user_ID]) or user_goal[user_ID]:
            continue
    # 현재 위치 받기 user_current_position 조회
        cur_r, cur_c = user_current_position[user_ID]
    # 목표로 하는 위치 받기 user_destination 조회
        dest_r,dest_c = user_destination[user_ID]
    # 비교 후 같다면 > user_goal 업데이트, matrix의 편의점 위치 락걸기
        if (cur_r,cur_c) == (dest_r,dest_c):
            user_goal[user_ID] = True
            matrix[dest_r][dest_c] = 2

def get_new_user(user_ID):
    # user_num보다 작거나 같고, 아직 출발 안한 사람을 대상으로 하기
    if user_ID > user_num:
        return
    if user_start[user_ID]:
        return
    # 해당 유저가 목표로 하는 편의점 위치 받기
    dest_r, dest_c = user_destination[user_ID]
    # 편의점 위치부터 시작해서 BFS 시작
    visited = set()
    visited.add((dest_r,dest_c))
    distance = 0
    bfs_queue = deque([(distance,dest_r,dest_c)])
    result = list()
    while len(bfs_queue) != 0:
        distance,cur_r,cur_c = bfs_queue.popleft()
        for dir in range(4):
            next_distance,next_r,next_c = distance+1,cur_r+dr[dir],cur_c+dc[dir]

            if in_range(next_r,next_c) and ((next_r,next_c) not in visited):
                visited.add((next_r, next_c))
                if matrix[next_r][next_c] == 1:
                    result.append((next_distance,next_r,next_c))
                else:
                    bfs_queue.append((next_distance,next_r,next_c))
    # 이때 BFS 상 베이스캠프가 있다면 모아두기
    # 모아둔 도착지를 전부 비교해, 행이작고 같다면 열이 작은 베이스 캠프 찾아 출발
    result.sort()
    distance,start_r,start_c = result[0]
    # user_current_position 업데이트,user_start 업데이트,matirx 업데이트
    user_current_position[user_ID] = (start_r,start_c)
    user_start[user_ID] = True
    matrix[start_r][start_c] = 2

while not end_game():
    # 시간이 흐름
    time += 1
    # 1. 격자에 있는 사람 편의점 방향으로 1칸 이동
    update_matrix()
    # 2. 편의점에 도착했다면 편의점 락걸기
    check_destination()
    # 3. 현재 시간 time <=user_num이라면 time에 해당하는 user ID가 베이스 캠프에 소환 후 락걸기
    get_new_user(time)

# 결과 출력
print(time)