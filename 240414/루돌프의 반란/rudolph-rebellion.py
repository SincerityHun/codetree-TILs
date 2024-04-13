# N*N 격자
# 각 위치 (r,c) -> (1,1)이 시작
# M개의 턴
# 매 턴마다 루돌프 움직 -> 산타 1번 -> 산타 2번 ....-> 산타 P번
# 이때, 기절 또는 죽은 산타는 움직일 수가 없음
# 거리는 (r1 - r2)^2 + (c1-c2)^2
# 1. 루돌프의 움직임
# 가장 가까운 산타를 향해 1칸
# 단, 탈락하지 않은 산타
# 가까운 산타 2명이상이라면, r그리고 c좌표가 큰 산타
# 8방향
# 2. 산타의 움직임
# 1번부터 P번까지
# 기절 혹은 죽은 산타는 이동 불가
# 다른 산타가 있는 칸 또는 게임판 밖 이동 불가
# 움직일 수 있는 칸이 없다면 그냥 안 움직임
# 있더라도 루돌프와 가까워지지 않으면 안 움직임
# 상하좌우 4방향 중 한 곳으로 이동 가능
# 우선순위 상,우,하,좌

# 3. 충돌
# 루돌프가 움직여서 충돌 -> 산타 C만큼 점수 얻고, 이동해온 방향으로 C칸 밀려남
# 산타가 움직여서 충돌 -> 산타 D만큼 점수 얻고, 자신이 이동해온 반대 방향으로 D칸 밀려남
# 밀려나면서 충돌이 중간에서는 일어나지 않음
# 도착한 위치가 밖이면 탈락
# 도착한 위치에 다른 산타 있으면 상호작용 시작

# 4. 상호작용
# 다른 사람이 민만큼 그대로 1칸 그 방향으로 이동
# 밖으로 밀려나면 탈락

# 5. 기절
# 충돌을 겪은 산타는 무조건 기절
# k번쨰턴에 충돌 -> k+2번쨰 턴부터 정상처리
# 기절해도 돌진 대상

# 6. 게임 종료
# M번의 턴에 걸쳐 루돌프, 산타 움직인 후 게임 끝
# 근데 P명의 산타가 모두 게임 탈락 -> 그 즉시 게임 종료
# 매 턴 이후 탈락 안한 산타에게 1점씩 추가 부여
# 각 산타가 얻은 최종 점수를 구하는 프로그램
row_num, turn_num, santa_num, power_rudol, power_santa = map(int, input().split())

# 통합 matrix -> 루돌프 위치(-1), 산타 위치(1~P번)를 가지고 있는 2차원 배열, 0이면 그냥 빈칸
matrix = [[0] * row_num for _ in range(row_num)]

# 루돌프 초기 위치
index_rudol = tuple(map(int, input().split()))
index_rudol = (index_rudol[0]-1,index_rudol[1]-1)
matrix[index_rudol[0]][index_rudol[1]] = -1

# 산타 초기위치
dict_santa = dict()
live_santa = [True]*(santa_num+1) # id번 산타가 살아있으면 live_santa[id] 는 True
stun_santa = [0]*(santa_num+1) # id번 산타가 스턴에 걸려있으면 0이 아님. 스턴에 걸리면 2를 넣는다.
for _ in range(santa_num):
    cur_num, cur_r, cur_c = tuple(map(int, input().split()))
    dict_santa[cur_num] = (cur_r-1, cur_c-1)
    matrix[cur_r-1][cur_c-1] = cur_num

# 범위 확인용
def in_range(r,c):
    return (0<=r<row_num) and (0<=c<row_num)
# 거리 계산하기
def cal_distance(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2
# 위부터 시계방향
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
# 상호작응을 시작하는 산타의 위치가 start_r, start_c 이며 dir방향으로 이동한 결과 어떤 상호작용에 해당하는 산타id를 리스트로 반환
def get_list_work(start_r,start_c,dir):
    result = list()
    cur_r, cur_c = start_r,start_c
    while in_range(cur_r,cur_c) and matrix[cur_r][cur_c] !=0:
        # 현재 위치 넣고
        result.append(matrix[cur_r][cur_c])
        # 그 다음 위치 탐색
        cur_r,cur_c = cur_r+dr[dir],cur_c+dc[dir]
    return result
def print_matrix(text):
    print(text)
    print("rudol index:",index_rudol)
    for i in range(row_num):  # TEST
        for j in range(row_num):
            print(matrix[i][j], end=" ")
        print()
    print()
# print("0회")
def move_rudol():
    global index_rudol
    # 현재 루돌프 위치 받기-> index rudol
    cur_rudol_r, cur_rudol_c = index_rudol
    # 현재 루돌프 위치 기준 가장 가깝게 살아있는 산타 id 찾아
    min_distance = row_num**2 + row_num**2 + 1
    min_r = -1
    min_c = -1
    for id in range(1,santa_num+1):
        if not live_santa[id]:
            continue
        santa_r,santa_c = dict_santa[id]
        distance = cal_distance(cur_rudol_r,cur_rudol_c,santa_r,santa_c)
        if (distance,-santa_r,-santa_c)<(min_distance,-min_r,-min_c):
            min_distance = distance
            min_r = santa_r
            min_c = santa_c
    # 살아 있는 산타가 없으면 나가야지
    if min_distance == 2*row_num:
        return
    # 8방향 거리 계산 후 가장 가까워지는 방향일때 거리 구해
    min_santa_r, min_santa_c = min_r, min_c
    min_dir = -1
    for dir in range(8):
        next_rudol_r,next_rudol_c = cur_rudol_r+dr[dir], cur_rudol_c+dc[dir]
        distance = cal_distance(next_rudol_r,next_rudol_c,min_santa_r,min_santa_c)
        if distance < min_distance:
            min_distance = distance
            min_dir = dir
    # 거리가 0이 아니라면 -> 루돌프 이동, index rudol이랑 matrix 동기화
    next_rudol_r,next_rudol_c =  cur_rudol_r+dr[min_dir], cur_rudol_c+dc[min_dir]
    if min_distance != 0:
        matrix[cur_rudol_r][cur_rudol_c] = 0
        index_rudol = (next_rudol_r,next_rudol_c)
        matrix[next_rudol_r][next_rudol_c] = -1
        return
    # 거리가 0이라면 일단 score 동기화
    min_santa_id = matrix[min_r][min_c]
    score[min_santa_id] += power_rudol
    # 가장 가깝게 산타가 밀려서 도착하는 index 계산
    next_santa_r, next_santa_c = min_santa_r+ power_rudol*dr[min_dir], min_santa_c+power_rudol*dc[min_dir]
    # 그 밖이라면 -> -> 루돌프 이동, 산타 죽음, index_rudol, matrix, live_santa
    if not in_range(next_santa_r,next_santa_c):
        matrix[cur_rudol_r][cur_rudol_c] = 0
        index_rudol = (next_rudol_r,next_rudol_c)
        matrix[next_rudol_r][next_rudol_c] = -1

        live_santa[min_santa_id] = False
        return

    victim_santa_id = matrix[next_santa_r][next_santa_c]
    # 그 index가 0이라면 -> 루돌프, 산타 이동, index_rudol, dict_santa,matrix, stun_santa 전부 동기화
    if victim_santa_id == 0:
        matrix[cur_rudol_r][cur_rudol_c] = 0
        index_rudol = (next_rudol_r,next_rudol_c)
        matrix[next_rudol_r][next_rudol_c] = -1
        dict_santa[min_santa_id] = (next_santa_r,next_santa_c)
        matrix[next_santa_r][next_santa_c] = min_santa_id
        stun_santa[min_santa_id] = 2
        return
    # 그 index가 1~santa_num 이라면
    victim_r,victim_c = next_santa_r,next_santa_c
    #       -> 상호작용으로 영향 받은 index 계산하기
    victim_list = get_list_work(victim_r,victim_c,min_dir)
    #       -> 루돌프 위치 업데이트, 첫 산타 업데이트, 상호작용 리스트 업데이트, index를 업데이트하고 + 새로운 위치에 추가만 하면됨
    matrix[cur_rudol_r][cur_rudol_c] = 0
    index_rudol = (next_rudol_r,next_rudol_c)
    matrix[next_rudol_r][next_rudol_c] = -1

    dict_santa[min_santa_id] = (next_santa_r,next_santa_c)
    matrix[next_santa_r][next_santa_c] = min_santa_id
    stun_santa[min_santa_id] = 2

    for id in victim_list:
        cur_victim_r,cur_victim_c = dict_santa[id]
        next_victim_r,next_victim_c = cur_victim_r+dr[min_dir],cur_victim_c+dc[min_dir]

        if not in_range(next_victim_r,next_victim_c):
            live_santa[id] =False
            return

        dict_santa[id] = (next_victim_r,next_victim_c)
        matrix[next_victim_r][next_victim_c] = id
        # 이떄, 마지막 아이템 같은 경우, 게임판 밖이면 live_santa 꼭 동기화

def move_santa(id):
    # 이 id는 살아있고, 스턴이 아님
    # 이 산타와 루돌프 사이의 거리 구하기
    cur_rudol_r,cur_rudol_c = index_rudol
    cur_santa_r, cur_santa_c = dict_santa[id]
    cur_distance = cal_distance(cur_santa_r,cur_santa_c,cur_rudol_r,cur_rudol_c)
    # 4방향 돌려가면서 거리가 제일 가까워지는 위치 찾기
    min_dir = -1
    for dir in [0,2,4,6]:
        next_santa_r,next_santa_c = cur_santa_r+dr[dir], cur_santa_c+dc[dir]
        # 이떄, matrix 상 양수면 안되고, 게임판 밖이면 당연히 안되겠지
        if (not in_range(next_santa_r,next_santa_c)) or (matrix[next_santa_r][next_santa_c] > 0):
            continue
        next_distance = cal_distance(next_santa_r,next_santa_c,cur_rudol_r,cur_rudol_c)
        if next_distance < cur_distance:
            cur_distance = next_distance
            min_dir = dir
    # 가까워지는 방향이 없으면 꺼져
    if min_dir == -1:
        return
    next_santa_r, next_santa_c = cur_santa_r + dr[min_dir], cur_santa_c + dc[min_dir]
    next_distance = cur_distance
    # distance가 0이 아니라면 -> 산타 이동, dict_santa, matrix 업데이트
    if next_distance != 0:
        matrix[cur_santa_r][cur_santa_c] = 0
        dict_santa[id] = (next_santa_r,next_santa_c)
        matrix[next_santa_r][next_santa_c] = id
        return
    # distance가 0이라면 일단 score 동기화
    score[id] += power_santa
    stun_santa[id] = 2
    # 이 산타가 밀려서 도착하는 index 계산
    min_dir = (min_dir + 4) % 8
    next_santa_r,next_santa_c = next_santa_r+power_santa * dr[min_dir],next_santa_c+power_santa*dc[min_dir]
    # 그 index가 밖이라면 -> 산타 죽음, live_santa, matrix 동기화
    if not in_range(next_santa_r,next_santa_c):
        live_santa[id] = False
        matrix[cur_santa_r][cur_santa_c] = 0
        return
    # 그 index가 0이라면 -> 산타 이동, dict_santa, matrix 전부 동기화
    victim_id = matrix[next_santa_r][next_santa_c]
    if victim_id == 0:
        matrix[cur_santa_r][cur_santa_c] = 0
        dict_santa[id] = (next_santa_r,next_santa_c)
        matrix[next_santa_r][next_santa_c] = id
        return
    if victim_id == id:
        return
    # 그 index가 1~santa_num이라면
    victim_r,victim_c = next_santa_r,next_santa_c
    # 상호작용으로 영향 받은 index들 계산
    victim_list = get_list_work(victim_r,victim_c,min_dir)
    # 그 index들 바탕으로 첫 산타 업데이트, 상호작용 리스트 업데이트
    matrix[cur_santa_r][cur_santa_c] = 0
    dict_santa[id] = (next_santa_r,next_santa_c)
    matrix[next_santa_r][next_santa_c] = id
    # 이때, 마지막 아이템이 게임판 밖이라면 live_santa 꼭 동기화
    for item_id in victim_list:
        item_r, item_c = dict_santa[item_id]
        next_item_r, next_item_c = item_r+dr[min_dir],item_c+dc[min_dir]
        if not in_range(next_item_r,next_item_c):
            live_santa[item_id] = False
            return

        dict_santa[item_id] = (next_item_r,next_item_c)
        matrix[next_item_r][next_item_c] = item_id
def end_game():
    for id in range(1,santa_num+1):
        if live_santa[id]:
            return False
    return True
# 시뮬레이션
score = [0]*(santa_num+1) # id번 산타의 점수는 score[id]
# print_matrix(f"{0}회") # TEST
for turn in range(turn_num):
    # print(turn+1,"회",index_rudol)

    # 1. 루돌프 이동
    move_rudol()
    if end_game():
        break
    # print_matrix(f"{turn+1}회") # TEST
    # 2. 산타 이동
    for id in range(1,santa_num+1):
        # 이미 죽었거나, 스턴스택이 남아있으면 스킵
        if (not live_santa[id]) or (stun_santa[id] > 0):
            continue
        move_santa(id)
    if end_game():
        break
    # print_matrix("") #TEST
    # 3. 탈락 안한 산타에게 1점씩 추가 -> live_santa 조회
    for id in range(1,santa_num+1):
        if not live_santa[id]:
            continue
        score[id] += 1
    # print(turn+1,"회 점수:",end=" ")
    # print(score) # TEST
    # print()
    # 4. 기절 스택이 0이 아닌 애들을 1씩 깍자 -> stun_santa 조회
    for id in range(1,santa_num+1):
        if (not live_santa[id]) or (stun_santa[id] == 0):
            continue
        stun_santa[id] -= 1
        # print(id,"의 스턴 스택을 이렇게 되었다.",stun_santa[id])# TEST
for id in range(1,santa_num+1):
    print(score[id],end=" ")