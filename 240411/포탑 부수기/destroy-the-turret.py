from collections import deque

row_num, col_num, time_limit = map(int, input().split())

# 포탑 정보 받기
matrix = []
for _ in range(row_num):
    matrix.append(list(map(int, input().split())))
# 현재 포탑 몇개 있는지
num = 0
for i in range(row_num):
    for j in range(col_num):
        if matrix[i][j] != 0:
            num += 1

# 언제 공격자 해봤는지 턴 저장 2차원 배열
attack_matrix = [[0] * col_num for i in range(row_num)]


# 공격자 찾기
def get_attack_index():
    # (r,c) = (-matrix,attack_matrix,행과열의합,열) 이 큰 애가 가져감
    # 그때 값 반환
    max_index = 0
    max_value = (-5000000, 0, 0, 0)
    for i in range(row_num):
        for j in range(col_num):
            temp_value = (-matrix[i][j], attack_matrix[i][j], i + j, j)
            if temp_value[0] == 0:
                continue
            if temp_value > max_value:
                max_value = temp_value
                max_index = (i, j)

    # 공격력 업데이트
    matrix[max_index[0]][max_index[1]] += (row_num + col_num)
    return max_index


# 공격 대상 찾기
def get_hurt_index(attack_index):
    # attack_index는 제외
    # (r,c) = (matrix,-attack_matrix,-행과열의합,-열)이 큰 애가 가져감
    # 그때값 반환
    max_index = 0
    max_value = (-1, 0, 0, 0)
    for i in range(row_num):
        for j in range(col_num):
            temp_value = (matrix[i][j], -attack_matrix[i][j], -(i + j), -j)
            if (temp_value[0] == 0) or ((i, j) == attack_index):
                continue
            if temp_value > max_value:
                max_value = temp_value
                max_index = (i, j)
    return max_index


# 공격 경로 찾기 우,하,좌,상, 우하,하좌,좌상,상우
dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, -1, 1]


# 그 다음 위치 찾기
def in_range(r, c, dir):
    next_r, next_c = (r + dr[dir]) % row_num, (c + dc[dir]) % col_num
    if matrix[next_r][next_c] == 0:
        return False
    return (next_r, next_c)


def get_attack_path(attack_index, hurt_index) -> list:
    # 1. 레이저
    bfs_queue = deque([attack_index])
    prev = {attack_index: None} # 각 노드의 이전 노드 저장
    
    while bfs_queue:
        cur_index = bfs_queue.popleft()
        if cur_index == hurt_index:
            break
        for dir in range(4):
            next_index = in_range(cur_index[0],cur_index[1],dir)
            if next_index and next_index not in prev:
                bfs_queue.append(next_index)
                prev[next_index] = cur_index
    path = []
    if hurt_index in prev:
        cur = hurt_index
        while cur:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        return path
    # 2. 포탑
    path.append(attack_index)
    for dir in range(8):
        next_index = in_range(hurt_index[0], hurt_index[1], dir)
        if (not next_index) or (next_index == attack_index):
            continue
        path.append(next_index)

    path.append(hurt_index)
    return path


# 공격 하기
def attack(attack_path,k):
    global num
    # 0번째의 공격력 받고 추가한뒤, matrix, attack_matrix 동기화, 0번째 제외
    attack_index = attack_path[0]
    attack_value = matrix[attack_index[0]][attack_index[1]]
    attack_matrix[attack_index[0]][attack_index[1]] = k
    # 경로상 index에는 나누기 2한 몫의 공격력 깍기, matrix 동기화
    length = len(attack_path)
    for i in range(1, length - 1):
        cur_r, cur_c = attack_path[i]
        matrix[cur_r][cur_c] -= (attack_value // 2)
        if matrix[cur_r][cur_c] <= 0:
            matrix[cur_r][cur_c] = 0
            num -= 1
    # 마지막 index에는 풀 공격력, matrix 동기화
    cur_r, cur_c = attack_path[-1]
    matrix[cur_r][cur_c] -= attack_value
    if matrix[cur_r][cur_c] <= 0:
        matrix[cur_r][cur_c] = 0
        num -= 1


# 포탑 정비하기
def update(attack_path):
    # attack_path을 제외하고, matrix가 0이 아니라면, 1씩 추가
    for i in range(row_num):
        for j in range(col_num):
            if ((i, j) not in attack_path) and matrix[i][j] != 0:
                matrix[i][j] += 1


# K턴 시작
for time in range(1, time_limit + 1):
    # 1. 공격자 찾기
    attack_index = get_attack_index()
    # 2. 공격 대상 찾기
    hurt_index = get_hurt_index(attack_index)
    # 3. 공격 경로 찾기
    attack_path = get_attack_path(attack_index, hurt_index)
    # 4. 공격 하기 -> 관련된 사람 뽑기
    attack(attack_path,time)
    # 공격 당한 후 1개 남으면 바로 아웃
    if num == 1:
        break
    # 5. 포탑 정비하기
    update(attack_path)

# 결과 출력
score = 0
for i in range(row_num):
    for j in range(col_num):
        if score < matrix[i][j]:
            score = matrix[i][j]

print(score)