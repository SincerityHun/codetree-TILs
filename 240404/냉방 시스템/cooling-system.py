import sys
from collections import defaultdict

n,m,k = map(int,sys.stdin.readline().rstrip().split()) # 격자 크기, 벽의 개수, 최소 시원함 정도
current_time = 0 # 흐른 시간

# map 받기, n**2
current_aircon = [list(),list(),list(),list()] # 왼,위,오,아래
current_work = [] # 1: 사무실
for i in range(n):
    temp = sys.stdin.readline().rstrip().split()
    for j in range(n):
        if temp[j] == '1':
            current_work.append((i,j))
        elif temp[j] != '0':
            current_aircon[int(temp[j])-2].append((i,j))
# 시원함 map
check_ice = []
for i in range(n):
    check_ice.append([0]*n)

# 벽 위치 저장 map
check_up_block = dict()
check_left_block = dict()
for i in range(m):
    r,c,d = map(int,sys.stdin.readline().rstrip().split())
    if d == 0: # 위
        check_up_block[(r-1,c-1)] = (r-2,c-1)
        check_up_block[(r-2,c-1)] = (r-1,c-1)
    else: # 왼
        check_left_block[(r-1,c-1)] = (r-1,c-2)
        check_left_block[(r-1,c-2)] = (r-1,c-1)

def out_range(next_index):
    r,c = next_index[0],next_index[1]
    return 0<=r<n and 0<=c<n

def check_block(cur_index,next_index):
    if out_range(next_index) == False:
        return True
    if check_up_block.get(cur_index) and check_up_block[cur_index] == next_index:
        return True # block 있음
    if check_left_block.get(cur_index) and check_left_block[cur_index] == next_index:
        return True
    return False

# dir: 0:왼,1:위,2:오,3:아래 + 4:위+왼, 5:위+오, 6:아래+오, 7:아래+왼 + 8:왼+위,9:오+위,10:오+아래,11:왼+아래
get_dir = [(0,-1),(-1,0),(0,1),(1,0),(1,0),(1,2),(3,2),(3,0),(0,1),(2,1),(2,3),(0,3)]
memo = set()
def get_dir_ice(dir,cur_index,value): # cur_index에서 dir 방향으로 옮겨가, check_ice에 value을 더하자
    global check_ice
    global memo
    # cur_index 에서 dir방향으로 갈 수 있는지 확인하고 데이터 넣어놓기
    next_index = 0
    flag = False
    if dir<4:
        # 그 다음 이동 장소 확인
        next_index = (cur_index[0]+get_dir[dir][0],cur_index[1]+get_dir[dir][1])
        # 그 다음 이동 장소가 밖이던가, 그 사이에 벽이 있으면 이동 불가
        if check_block(cur_index,next_index) == False and next_index not in memo:
            flag = True
            # 할당
            check_ice[next_index[0]][next_index[1]] += value
            # 하나 감소하고
            value -= 1
            if value == 0:
                return

    else:
        # 체크 장소 확인
        check_index = (cur_index[0]+get_dir[get_dir[dir][0]][0],cur_index[1]+get_dir[get_dir[dir][0]][1])
        next_index = (check_index[0]+get_dir[get_dir[dir][1]][0],check_index[1]+get_dir[get_dir[dir][1]][1])
        # cur -> check 가능한지 확인
        if check_block(cur_index,check_index) == False and check_block(check_index,next_index) == False and next_index not in memo:
            flag = True
            check_ice[next_index[0]][next_index[1]] += value
            value -= 1
            if value == 0:
                return
    if flag:
        memo.add(next_index)
        # 그다음 장소로 보내기
        if dir in (0,4,7):
            get_dir_ice(0, next_index, value)
            get_dir_ice(4, next_index,value)
            get_dir_ice(7, next_index, value)
        elif dir in (1,8,9):
            get_dir_ice(1, next_index, value)
            get_dir_ice(8, next_index, value)
            get_dir_ice(9, next_index, value)
        elif dir in (2,5,6):
            get_dir_ice(2, next_index, value)
            get_dir_ice(5, next_index, value)
            get_dir_ice(6, next_index, value)
        else:
            get_dir_ice(3, next_index, value)
            get_dir_ice(10, next_index, value)
            get_dir_ice(11, next_index, value)

def get_ice():
    global current_aircon
    global memo
    for dir in range(4): # 0:왼,1:위,2:오,3:아래
        # 특정 방향 업데이트
        for index in current_aircon[dir]:
            memo.clear()
            next_index = (index[0] + get_dir[dir][0], index[1] + get_dir[dir][1])
            check_ice[next_index[0]][next_index[1]] += 5
            get_dir_ice(dir,next_index,4) # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
            if dir == 0:
                get_dir_ice(4, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
                get_dir_ice(7, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
            elif dir == 1:
                get_dir_ice(8, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
                get_dir_ice(9, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
            elif dir ==2:
                get_dir_ice(5, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
                get_dir_ice(6, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
            else:
                get_dir_ice(10, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
                get_dir_ice(11, next_index, 4)  # dir방향으로 한칸 움직인 다음에 value을 넣어줘야함
def update_single_ice(a_index,b_index,database):
    global check_ice
    a = check_ice[a_index[0]][a_index[1]]
    b = check_ice[b_index[0]][b_index[1]]
    if a > b:
        margin = (a-b) // 4
        if margin > 0:
            database[a_index] -= margin
            database[b_index] += margin
    else:
        margin = (b - a) // 4
        if margin > 0:
            database[b_index] -= margin
            database[a_index] += margin
def update_ice():
    cal_ice = defaultdict(int) # 계산용
    # (r,c) -> (r,c+1),(r+1,c)
        # check_block
        # 차이 // 4 1이상인 경우에만 default dict에 저장
    for i in range(n):
        for j in range(n):
            if check_block((i,j),(i,j+1)) == False:
                update_single_ice((i,j),(i,j+1),cal_ice)
            if check_block((i,j),(i+1,j)) == False:
                update_single_ice((i, j), (i+1, j), cal_ice)
    # defualtdict을 활용해 check_ice 업데이트
    for index,value in  cal_ice.items():
        check_ice[index[0]][index[1]] += value
def decrease_ice():
    global check_ice
    # 1행
    for i in range(n):
        if check_ice[0][i]:
            check_ice[0][i] -= 1
    # 그 외행
    for i in range(1,n-1):
        if check_ice[i][0]:
            check_ice[i][0] -= 1
        if check_ice[i][n-1]:
            check_ice[i][n-1] -=1
    # 마지막행
    for i in range(n):
        if check_ice[n-1][i]:
            check_ice[n-1][i] -= 1
def simulate():
    # 1. 바람 쏘기
    get_ice()
    # 2. 시원함 계산하기
    update_ice()
    # 3. 외벽 감소하기
    decrease_ice()
def check_ok():
    global current_time
    global k
    # simulate 했으니까 시간 증가
    current_time += 1
    # 사무실 시원함 체크
    for x in current_work:
        if check_ice[x[0]][x[1]] < k:
            return False
    # 전부 돼? 참 반환
    return True

while current_time <= 100:
    simulate()
    if check_ok():
        print(current_time)
        break
if current_time == 101:
    print(-1) # 100분이 넘는 경우