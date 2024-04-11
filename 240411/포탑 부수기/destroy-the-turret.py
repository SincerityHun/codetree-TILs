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
        if not matrix[i][j]:
            num += 1

# 언제 공격자 해봤는지 턴 저장 2차원 배열
attack_matrix = [[0] * col_num for i in range(row_num)]


# 공격자 찾기
def get_attack_index():
    # (r,c) = (-matrix,attack_matrix,행과열의합,열) 이 큰 애가 가져감
    # 그때 값 반환
    max_index = 0
    max_value = (-5001, 0, 0, 0)
    for i in range(row_num):
        for j in range(col_num):
            temp_value = (-matrix[i][j], attack_matrix[i][j], i + j, j)
            if not temp_value[0]:
                continue
            if temp_value > max_value:
                max_value = temp_value
                max_index = (i, j)

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
            if (not temp_value[0]) or ((i, j) == attack_index):
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
    # BFS
    # 1. 레이저
    path = list()
    bfs_list = deque()
    bfs_list.append([attack_index])

    while len(bfs_list):
        cur_path = bfs_list.popleft()
        visited = set(cur_path)
        cur_r, cur_c = cur_path[-1]
        if (cur_r, cur_c) == hurt_index:
            path = cur_path
            break
        for dir in range(4):
            next_index = in_range(cur_r, cur_c, dir)
            if (not next_index) or (next_index in visited):
                continue
            bfs_list.append(cur_path + [next_index])
    if path:
        return path
    # 2. 포탑
    path.append(attack_index)
    for dir in range(8):
        next_index = in_range(hurt_index[0], hurt_index[1], dir)
        if not next_index:
            continue
        path.append(next_index)

    path.append(hurt_index)
    return path
    # 0번 attack_index
    # 그 사이는 경로상 혹은 그냥 피해받은 애들
    # 마지막 hurt_index


# 공격 하기
def attack(attack_path):
    global num
    # 0번째의 공격력 받고추가한뒤,matrix,attack_matrix 동기화, 0번째 제외
    attack_index = attack_path[0]
    attack_value = matrix[attack_index[0]][attack_index[1]]
    attack_matrix[attack_index[0]][attack_index[1]] += 1
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
            if ((i, j) not in attack_path) and matrix[i][j]:
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
    attack(attack_path)
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