import sys

# L: 체스판의 크기, N: 기사의 수, Q: 명령의 수
L, N, Q = map(int, sys.stdin.readline().rstrip().split())
# L*L 체스판 정보 받기 -> 0:빈칸, 1:함정, 2:벽
matrix = []
for _ in range(L):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
# L*L 기사 위치 정보 2차원 배열 및 이동 방식
soldier_matrix = [[-1] * L for _ in range(L)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# N개의 줄에 거쳐서 (r,c,h,w,k) -> k:기사의 체력
soldier_dict = dict()
soldier_live = [True] * N  # 살아있다면 True
soldier_damage = [0] * N  # 받은 데미지

for i in range(N):
    r, c, h, w, k = tuple(map(int, sys.stdin.readline().rstrip().split()))
    soldier_dict[i] = (r - 1, c - 1, h, w, k)
    for j in range(r - 1, r - 1 + h):
        for k in range(c - 1, c - 1 + w):
            soldier_matrix[j][k] = i


# 벽, 외부를 확인하는 함수
def in_range(r, c):
    return (0 <= r < L) and (0 <= c < L) and (matrix[r][c] != 2)


# info 을 바탕으로 soldier_matrix에 전부 집어 넣을 수 있는지 확인하는 함수 -> 성공하면 True 실패하면 False
def check_soldier_matrix(info):
    r, c, h, w, k = info
    if in_range(r, c) and in_range(r + h - 1, c + w - 1):
        for i in range(r, r + h):
            for j in range(c, c + h):
                if matrix[i][j] == 2:
                    return False
    return True


# 함정 수에 따라 데미지 계산하는 함수
def cal_damage(soldier_index):
    ans = 0
    cur_r, cur_c, h, w = soldier_dict[soldier_index][0], soldier_dict[soldier_index][1], soldier_dict[soldier_index][2], \
    soldier_dict[soldier_index][3]
    for i in range(cur_r, cur_r + h):
        for j in range(cur_c, cur_c + w):
            if matrix[i][j] == 1:
                ans += 1
    return ans


# 넣는게 가능하다고 판단되었을 때, 넣기-> 기존 위치에서 dir만큼 움직이면 info의 위치를 id가 갖는다.
def put_soldier_matrix(info, id, dir):
    r, c, h, w, k = info
    # 지우고
    if dir == 0:
        target_r =r + h
        for j in range(c,c+w):
            soldier_matrix[target_r][j] = -1
    elif dir == 1:
        target_c = c-1
        for j in range(r,r+h):
            soldier_matrix[j][target_c] = -1
    elif dir == 2:
        target_r = r -1
        for j in range(c, c + w):
            soldier_matrix[target_r][j] = -1
    elif dir == 3:
        target_c = c + w
        for j in range(r, r + h):
            soldier_matrix[j][target_c] = -1
    # 새로 넣으면서 숫자 계산
    score = 0
    for i in range(r, r + h):
        for j in range(c, c + w):
            soldier_matrix[i][j] = id
            if matrix[i][j] == 1:
                score += 1
    return score


def add_next_set(next_check_temp_list, next_r, next_c):
    if in_range(next_r, next_c):
        soldier_index = soldier_matrix[next_r][next_c]
        if soldier_index != -1:
            next_check_temp_list.add(soldier_index)
        return True
    else:
        return False


# Q개의 줄에 거쳐서 (i,d) -> i번 기사에게 방향 d로 한 칸 이동, 1<=i<=N, d:0,1,2,3 : 위 오 아 왼
for _ in range(Q):
    i, d = map(int, sys.stdin.readline().rstrip().split())
    i -= 1
    # i번 기사가 d 방향으로 이동하기 위해 고려해야 되는 기사 목록 찾기
    if not soldier_live[i]:
        continue
    check_global_list = list()  # 밀수 있다면 얘네 밀면 돼
    check_temp_list = set()  # 얘네가 밀리는지 체크해야해
    check_global_list.append(i)
    check_temp_list.add(i)
    flag = True  # 밀 수 있다면 True
    while len(check_temp_list) != 0:
        next_check_temp_list = set()
        for item in check_temp_list:
            cur_r, cur_c, h, w, k = soldier_dict[item]
            # d에 따라 그 쪽 방향과 맞닿아있는 칸을 확인해야된다.
            # 그쪽 방향에 벽, 또는 외부라면? -> flag = False, break
            # 그쪽 방향에 기사가 있다면? -> check_temp_list를 대체 + check_global_list을 추가
            if d == 0:
                for j in range(cur_c, cur_c + w):
                    next_r, next_c = cur_r - 1, j
                    if not add_next_set(next_check_temp_list, next_r, next_c):
                        flag = False
                        break
            elif d == 1:
                for j in range(cur_r, cur_r + h):
                    next_r, next_c = j, cur_c + w
                    if not add_next_set(next_check_temp_list, next_r, next_c):
                        flag = False
                        break
            elif d == 2:
                for j in range(cur_c, cur_c + w):
                    next_r, next_c = cur_r + h, j
                    if not add_next_set(next_check_temp_list, next_r, next_c):
                        flag = False
                        break
            elif d == 3:
                for j in range(cur_r, cur_r + h):
                    next_r, next_c = j, cur_c - 1
                    if not add_next_set(next_check_temp_list, next_r, next_c):
                        flag = False
                        break
        if not flag:
            break
        check_temp_list.clear()
        check_temp_list.update(next_check_temp_list)
        check_global_list.extend(list(check_temp_list))
    # 해당 기사 목록을 역으로 해서 하나씩 이동하기
    if flag:
        # 이미 한번 민건 또 밀면 안댐
        memo = set()
        # x는 현재 밀어야 하는 기사의 ID
        for x in check_global_list[::-1]:
            if x in memo:
                continue
            else:
                memo.add(x)
            cur_r, cur_c, h, w, k = soldier_dict[x]
            next_r, next_c = cur_r + dr[d], cur_c + dc[d]
            info = (next_r,next_c,h,w,k)
            soldier_dict[x] = info
            temp_score = put_soldier_matrix(info, x, d)
            if x !=i:
                soldier_damage[x] += temp_score

        # 이동 후 죽은거 처리하기
        for i in range(N):
            if soldier_live[i] and soldier_dict[i][4]<= soldier_damage[i]:
                soldier_live[i] = False
                r,c,h,w,k = soldier_dict[i]
                for j in range(r,r+h):
                    for k in range(c,c+w):
                        soldier_matrix[j][k] = -1


# 생존한 기사들이 받은 데미지의 합
ans = 0
for i in range(N):
    if soldier_live[i]:
        ans += soldier_damage[i]
print(ans)