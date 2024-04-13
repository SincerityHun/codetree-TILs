# 2^n * 2^n 사이즈 빙하 회전
# 각각의 얼음 -> 인접 회전성
# L -> 2^L* 2^L만큼씩 선택하여 2^(L-1) * 2 ^(L-1)을 잘라 4등분 후 회전
#   -> 총 몇개 생기지 -> 4^(N-L)
# 레벨 0 -> 얼음 위치 안변함
# 레벨 1 -> 2*2를 잘라, 1*1을 사등분해서 시계방향 회전
# 레벨 2 -> 2*2
# 회전 후 -> 빙하에 속한 얼음이 녹음
# 상하좌우 인접한 칸에 얼음이 3개 이상 있는 경우 녹지 않음
# 그렇지 않은 경우 1이 줄어든다.
# 물론 범위 밖은 없다고 생각해야하며
# 얼음 녹는건 동시 처리
# 모든 회전을 끝내고 난 뒤 남아있는 빙하의 총양, 가장 큰 얼음군집의 크기 -> 연결된 칸의 집합의 크기
from collections import deque

row_factor, turn_num = map(int, input().split())
row_num = 2 ** row_factor

# 얼음 정보 받기
ice_matrix = []
for i in range(row_num):
    ice_matrix.append(list(map(int, input().split())))

# 회전 정보 받기
turn_factor_list = list(map(int, input().split()))
melt_matrix = [[False] * row_num for _ in range(row_num)]  # False면 녹지 않음
# 상,하,좌,우
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 범위 체크 함수
def in_range(r, c):
    return (0 <= r < row_num) and (0 <= c < row_num)


# 시뮬레이션 시작
for turn in range(turn_num):
    # 회전 단위 계산하기
    cur_row = 2 ** turn_factor_list[turn]
    if cur_row != 1:
        # 회전 단위별로 돌면서 회전 시키기
        for i in range(0, row_num, cur_row):
            for j in range(0, row_num, cur_row):
                small_row = 2 ** (turn_factor_list[turn] - 1)
                # 돌릴 인덱스 받기
                id_matrix = [[0] * 2 for _ in range(2)]
                id_r = 0
                id_c = 0
                for start_i in range(i, i + cur_row, small_row):
                    for start_j in range(j, j + cur_row, small_row):
                        id_matrix[id_r][id_c] = (start_i, start_j)
                        id_c +=1
                    id_r +=1
                    id_c = 0
                id_matrix = list(map(list, zip(*id_matrix[::-1])))
                # 돌려서 복사해넣기
                temp_matrix = [[0] * cur_row for _ in range(cur_row)]
                temp_index = [(0,0),(0,small_row),(small_row,0),(small_row,small_row)]
                cur_temp = 0
                for small_i in range(2):
                    for small_j in range(2):
                        start_r, start_c = id_matrix[small_i][small_j]
                        temp_r,temp_c = temp_index[cur_temp][0],temp_index[cur_temp][1]
                        cur_temp+=1
                        for copy_r in range(start_r, start_r + small_row):
                            for copy_c in range(start_c, start_c + small_row):
                                temp_matrix[temp_r + copy_r-start_r][temp_c + copy_c-start_c] = ice_matrix[copy_r][copy_c]
                # 원본 슛
                for copy_r in range(i, i + cur_row):
                    for copy_c in range(j, j + cur_row):
                        ice_matrix[copy_r][copy_c] = temp_matrix[copy_r - i][copy_c - j]
    # 회전 끝났으면 모든 칸의 주위를 계산해서 melt_matrix에 넣어두기
    for i in range(0, row_num):
        for j in range(0, row_num):
            cur_r, cur_c = i, j
            if ice_matrix[cur_r][cur_c] == 0:
                continue
            count = 0
            for dir in range(4):
                next_r, next_c = cur_r + dr[dir], cur_c + dc[dir]
                if in_range(next_r, next_c) and ice_matrix[next_r][next_c] != 0:
                    count += 1
            if count < 3:
                melt_matrix[cur_r][cur_c] = True
            else:
                melt_matrix[cur_r][cur_c] = False
    # 모든 칸 조회 + 칸의 얼음이 있으면 melt_matrix에 따라서 True면 1깍기
    for i in range(0, row_num):
        for j in range(0, row_num):
            if (ice_matrix[i][j] > 0) and melt_matrix[i][j]:
                ice_matrix[i][j] -= 1
# 남아있는 빙하의 총양 + 가장 큰 얼음 군집의 크기 출력
global_visited = set()
max_size_of_group = 0
sum_ice = 0
for i in range(row_num):
    for j in range(row_num):
        if (i, j) in global_visited or ice_matrix[i][j] == 0:
            continue
        local_visited = set()
        local_visited.add((i, j))
        bfs_queue = deque([(i, j)])
        while len(bfs_queue) != 0:
            cur_r, cur_c = bfs_queue.popleft()
            sum_ice += ice_matrix[cur_r][cur_c]
            for dir in range(4):
                next_r, next_c = cur_r + dr[dir], cur_c + dc[dir]
                if in_range(next_r, next_c) and ((next_r, next_c) not in local_visited) and (
                        ice_matrix[next_r][next_c] != 0):
                    local_visited.add((next_r, next_c))
                    bfs_queue.append((next_r, next_c))

        max_size_of_group = max(max_size_of_group, len(local_visited))
        global_visited.update(local_visited)

print(sum_ice)
print(max_size_of_group)