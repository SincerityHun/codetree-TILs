MAX_T = 25 # Max Trial
MAX_N = 4  # MAX ROW&COLLUM
DIR_NUM = 8 # Monster Direction Number
P_DIR_NUM = 4 # Pacman Direction Number
MAX_DECAY = 2 # Decay Number

n = 4 # ROW & COlumn
m, t = tuple(map(int,input().split()))

px,py = tuple(map(int,input().split()))
px -= 1; py-= 1

#T턴에 (r,c)의 3번 방향을 보고 있는 Monster가 3? monster[T][r][c][3] = 3
monster = [
    [
        [
            [0]*DIR_NUM
            for _ in range(n)
        ]
        for _ in range(n)
    ]
    for _ in range(MAX_T + 1)
]

# (x,y) 위치에서 썩기 t초 전인 시체가 3개 있어? dead[x][y][t] = 3
dead = [
    [
        [0] * (MAX_DECAY + 1)
        for _ in range(n)
    ]
    for _ in range(n)
]

# 몬스터를 위한 방향 정의
dxs =[-1,-1,0,1,1,1,0,-1]
dys = [0,-1,-1,-1,0,1,1,1]

# 팩맨을 위한 방향 정의 상 좌 하 우, 즉 0일수록 우선순위 높음
p_dxs = [-1,0,1,0]
p_dys = [0,-1,0,1]

# 현재 몇번째 턴인지
t_num = 1

# 영역에 있는지
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

# 가려는 위치에 몬스터 시체도 없고 팩맨도 없으면 이동 가능
def can_go(x,y):
    return in_range(x,y) and dead[x][y][0] == 0 and dead[x][y][1] == 0 and (x,y)!=(px,py)

for _ in range(m):
    mx, my, mdir = tuple(map(int,input().split()))
    monster[0][mx-1][my-1][mdir-1] += 1
def get_next_pos(x,y,move_dir):
    # 현재 위치에서 가능한 위치 찾기
    for c_dir in range(DIR_NUM):
        next_dir = (move_dir + c_dir) % DIR_NUM
        nx,ny = x + dxs[next_dir],y+dys[next_dir]
        if can_go(nx,ny):
            return (nx,ny,next_dir)
    # 이동 불가
    return (x,y,move_dir)

def move_m():
    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                x,y,next_dir = get_next_pos(i,j,k)
                monster[t_num][x][y][next_dir] += monster[t_num-1][i][j][k]

def get_killed_num(dir1,dir2,dir3):
    x,y = px,py
    killed_num = 0

    # 방문한적 있는지 기록
    v_pos = []

    for move_dir in [dir1,dir2,dir3]:
        nx,ny = x + p_dxs[move_dir],y+p_dys[move_dir]
        # 범위 밖이면 NOPE
        if not in_range(nx,ny):
            return -1
        # 이미 계산한 곳에 대해서 중복 계산 안함
        if (nx,ny) not in v_pos:
            killed_num += sum(monster[t_num][nx][ny])
            v_pos.append((nx,ny))
        x,y = nx, ny
    return killed_num
def do_kill(best_route):
    global px,py

    dir1, dir2, dir3 = best_route
    for move_dir in [dir1,dir2,dir3]:
        nx, ny = px + p_dxs[move_dir],py + p_dys[move_dir]
        # 현재 maze에 있는 모든 방향에 대해서?
        for i in range(DIR_NUM):
            # dead에 넣고
            dead[nx][ny][MAX_DECAY] += monster[t_num][nx][ny][i]
            # monster 비우기
            monster[t_num][nx][ny][i] = 0
        
        # 그 다음 방향
        px,py = nx,ny
def move_p():
    max_cnt = -1
    best_route = (-1,-1,-1)

    # 우선순위부터 뒤지기 시작
    for i in range(P_DIR_NUM):
        for j in range(P_DIR_NUM):
            for k in range(P_DIR_NUM):
                m_cnt = get_killed_num(i,j,k)
                # 우선순위가 높은걸 고려함 여기서
                if m_cnt > max_cnt:
                    max_cnt = m_cnt
                    best_route = (i,j,k)

    # 실제 죽이기
    do_kill(best_route)
def decay_m():
    for i in range(n):
        for j in range(n):
            for k in range(MAX_DECAY):
                dead[i][k][k] = dead[i][j][k+1]
            dead[i][j][MAX_DECAY] = 0
def add_m():
    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                monster[t_num][i][j][k] += monster[t_num-1][i][j][k]
def simulate():
    # 매 초를 기록해서 굳이 알을 카피할 필요가 없음
    # 각 칸에 몬스터 움직이고
    move_m()
    # 팩맨을 이동시키고
    move_p()
    # 시체들을 썩히고
    decay_m()
    # 몬스터가 복제
    add_m()

def count_monster():
    global t
    cnt = 0

    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                cnt += monster[t][i][j][k]
    return cnt

while t_num <= t:
    simulate()
    t_num+= 1

print(count_monster())