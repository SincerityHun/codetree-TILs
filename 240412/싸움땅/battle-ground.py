# N*N 격자
# 각각의 격자 -> 무기가 있을 수도 있음
# 없는 곳에는 플레이어가 있고 각자 능력치가 있음, 플레이어도 없을 수 있음
# 초기 능력치는 모두 다르다...
# 빨 -> 총 공격력 혹은 플레이어의 초기 능력치
# 노 -> 플레이어 번호
# 1-1: 첫번쨰 플레이어부터 플레이어는 현재 방향대로 한칸 이동
    # 이떄, 방향이 격자를 벗어나면, 반대 방향으로 바꾸고 1이동
    # 이떄 이동한 방향에 플레이어가 없다면, 총이 있는지 호가인
        # 총이 있는 경우 -> 총 획득
        # 이미 플레이어가 총이 있으면, 더 쎈총을 획득하고 나머지 총들!!은 냅둠
    # 이동한 방향에 플레이어가 있다면, 싸움
        # 능력치 + 총의 공격력 합을 비교해 더 큰 플레이어가 이김
        # 이 수치가 같다면, 플레이어의 초기 능력치가 높은 애
        #  이김 -> (능력치 + 총의 공격력) 차이만큼 포인트로 획득, 진애가 총 떨구고 간거랑 비교해서 더 쎈거 가져감
        # 짐 -> 본인이 가지고 있는 총 해당 격자에 내려놓음
            #-> 원래 방향대로 한칸 더 이동
            # 이때, 또 플레이어가 있거나 격자 범위 밖이라면 시계방향 90도 회전
            # 빈칸 보이는 순간 이동
            # 물론 이때도, 총이 있다면, 가장 공격력이 높은 총 획득하고 내려놓음

# 저렇게 1번부터 n번까지 진행하면 1라운드 끝남
# k라운드 진행하고 각 플레이어 들이 획득한 포인트를 출력하셈

row_num, user_num, round_num = map(int,input().split())

# 총 놓여 있는 정보 받기
matrix = [[] for i in range(row_num)]
for row in range(row_num):
    temp = list(map(int,input().split()))
    for i in range(row_num):
        if temp[i] != 0:
            matrix[row].append([temp[i]])
        else:
            matrix[row].append([])
# 유저 정보 받기
user_matrix = [[-1]*row_num for row in range(row_num)] # 얘는 동기화
user_dict = dict() # (r,c,dir,power,gun) , gun = 0이면 안줍고 있는거임, 무조건 현장 반응
dr = [-1,0,1,0] #상, 우, 하, 좌
dc = [0,1,0,-1]
for id in range(user_num):
    r,c,dir,power = map(int,input().split())
    user_matrix[r-1][c-1] = id
    user_dict[id] = (r-1,c-1,dir,power,0)
# 범위 체크
def in_range(r,c):
    return (0<=r<row_num) and(0<=c<row_num)
# 방향만 맞으면 고
def get_next_index(user_ID):
    cur_r,cur_c,dir,power,gun= user_dict[user_ID]
    user_matrix[cur_r][cur_c] = -1 # 이전 위치 지우기
    next_r,next_c = cur_r+dr[dir],cur_c+dc[dir]
    if in_range(next_r,next_c):
        user_dict[user_ID] = (next_r,next_c,dir,power,gun)
        return user_dict[user_ID]
    next_dir = (dir+2)%4
    next_r,next_c = cur_r+dr[next_dir],cur_c+dc[next_dir]
    user_dict[user_ID] = (next_r,next_c,next_dir,power,gun)
    return user_dict[user_ID]

def get_loser_index(cur_r,cur_c,cur_dir):
    next_r,next_c = cur_r+dr[cur_dir],cur_c+dc[cur_dir]
    while (not in_range(next_r,next_c)) or (user_matrix[next_r][next_c] != -1):
        cur_dir = (cur_dir + 1) % 4
        next_r, next_c = cur_r + dr[cur_dir], cur_c + dc[cur_dir]
    return next_r,next_c,cur_dir
# 시뮬레이션 시작
score = [0]*user_num
for k in range(round_num):
    # 0~user_num-1 유저 동안 진행
    for user_id in range(user_num):
        # 1. 유저가 다음에 움직일 위치 탐색-> user_dict 업데이트, 이전 위치의 user_matrix 지움
        next_r,next_c,cur_dir,power,gun = get_next_index(user_id)
        # 2. 다음에 움직일 위치에 플레이어가 없는 경우
        competer_id = user_matrix[next_r][next_c]
        if competer_id == -1:
            # 총이 있는 경우
            next_gun = gun
            if len(matrix[next_r][next_c]) != 0:
                # 가지고 있는 총을 해당 리스트에 넣어서 더 쎈총 획득
                # matrix[next_r][next_c] 업데이트 후 가장 큰거 뽑기
                matrix[next_r][next_c].append(gun)
                matrix[next_r][next_c].sort()
                next_gun = matrix[next_r][next_c].pop()
            # user_matrix,user_dict 업데이트
            user_dict[user_id] = (next_r, next_c, cur_dir, power, next_gun)
            user_matrix[next_r][next_c] = user_id
        # 3. 다음에 움직일 위치에 플레이어가 있는 경우
        else:
            # 상대인 유저 받기, user_matrix 조회
            c_r,c_c,c_dir,c_power,c_gun = user_dict[competer_id]
            # 누가 이기는지 확인, (합, 초기능력치) 가 큰 애가 이김, user_dict 조회
            if (power+gun,power) > (c_power+c_gun,c_power):
                winner_id = user_id
                loser_id = competer_id
                value = (power+gun) - (c_power+c_gun)
            else:
                winner_id = competer_id
                loser_id = user_id
                value = (c_power+c_gun) - (power+gun)
            winner_r, winner_c, winner_dir, winner_power, winner_gun = user_dict[winner_id]
            loser_r, loser_c, loser_dir, loser_power, loser_gun = user_dict[loser_id]
            # 이긴 플레이어 -> 합의 차이만큼 포인트 획득, score 업데이트
            score[winner_id] += value
            # 진 플레이어 -> 새로 이동 가능한 방향을 탐색해, 범위 안 + 플레이어가 없는 곳
            matrix[loser_r][loser_c].append(loser_gun)
            loser_gun = 0
            loser_r,loser_c,loser_dir = get_loser_index(loser_r,loser_c,loser_dir)
            # -> 현재 위치에 총 내려놔, matrix 업데이트
            # -> 다음 위치에 총이 있다면, 총 주워, 이미 전에 내려놨다고 가정하고 matrix 업데이트, user_dict, user_matrix 업데이트
            if len(matrix[loser_r][loser_c]) != 0:
                matrix[loser_r][loser_c].sort()
                loser_gun = matrix[loser_r][loser_c].pop()
            user_matrix[loser_r][loser_c] = loser_id
            user_dict[loser_id] = (loser_r,loser_c,loser_dir,loser_power,loser_gun)
            # 이긴 플레이어 -> 총 업데이트,matrix 업데이트
            matrix[winner_r][winner_c].append(winner_gun)
            matrix[winner_r][winner_c].sort()
            winner_gun = matrix[winner_r][winner_c].pop()
            # -> 위치 업데이트
            user_matrix[winner_r][winner_c] = winner_id
            user_dict[winner_id] =(winner_r,winner_c,winner_dir,winner_power,winner_gun)

for i in range(user_num):
    print(score[i],end=" ")
print()