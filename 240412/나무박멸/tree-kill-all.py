# N*N
# 1. 나무 성장 -> 인접 4칸 + 동시
# 2. 벽, 다른 나무, 제초제 모두 없으면 번식
    # ( 현재 나무 그루 수 ) // (번식 가능한 칸의 개수) 씩 번식을 함
    # 동시에

# 3. 가장 많은 나무가 박멸되는 칸에 제초제,
# 없는 칸 -> 박멸 X
# 있는 칸 -> 4개의 대각선 + k칸
    # 전파 되는 도중 벽이 있거나 나무가 아얘 없다면 끊김
    # c년만큼 제초제 남아있고 C+1년될때 사라짐
    # 그 칸 포함
# 죽는 나무 , 행, 열 이 젤 작은 얘

# 3개끝나면 1년 지남
# m년동안 박멸한 나무의 그루 수
row_num, time_limit, spread_size, remain_dead = map(int,input().split())

matrix = [] # 0-> 빈칸, 음수-> 제초제, 이외 숫자는 나무가 있음
for row in range(row_num):
    matrix.append(list(map(int,input().split())))
# OUT OF INDEX, 벽 또는 제초제가 이미 있는 경우
def in_range(r,c):
    return (0<=r<row_num) and (0<=c<row_num)
# 벽
wall_set = set()
for row in range(row_num):
    for col in range(row_num):
        if matrix[row][col] == -1:
            wall_set.add((row,col))

# 박멸 index 상,우,하,좌, 상우, 우하, 하좌, 좌상
dr = [-1,0,1,0,-1,1,1,-1]
dc = [0,1,0,-1,1,1,-1,-1]
score =0
for time in range(time_limit):
    cal_metrix = [[0] * row_num for i in range(row_num)]
    dead_dict = dict()
    # 1. 나무 성장
    # matrix 조회
    for row in range(row_num):
        for col in range(row_num):
            # 기존 나무들 탐색
            if  matrix[row][col] <= 0:
                continue
            # 기존 나무 주위 나무 탐색 후 개수 계산
            count = 0
            for dir in range(4):
                next_r,next_c = row+dr[dir],col+dc[dir]
                if in_range(next_r,next_c) and (matrix[next_r][next_c] > 0):
                    count += 1
            # 그 개수만큼 기존 숲에 나무 추가-> matrix 업데이트
            matrix[row][col] += count

    # 2. 번식
    # matrix 조회
    for row in range(row_num):
        for col in range(row_num):
            # 기존 숲 탐색
            if matrix[row][col] <= 0:
                continue
            # 기존 숲 주변에 번식 가능한 -> 벽, 다른나무, 제초제 모두 없는 칸 index찾기
            count = 0
            index = set()
            for dir in range(4):
                next_r,next_c = row+dr[dir],col+dc[dir]
                if in_range(next_r,next_c) and matrix[next_r][next_c] == 0:
                    count += 1
                    index.add((next_r,next_c))

            # (기존 숲 나무 그루수)//(번식 가능한 칸의 개수)만큼 번식 -> cal_matrix 업데이트
            if count == 0:
                continue

            temp_score = matrix[row][col] // count
            for (r,c) in index:
                cal_metrix[r][c] += temp_score

    # 전부 조회 끝났으면 cal_matrix을 matrix에 반영 및 초기화
    for row in range(row_num):
        for col in range(row_num):
            if matrix[row][col] !=0:
                continue
            matrix[row][col] = cal_metrix[row][col]


    # 3. 제초제 -> -(c+1)
    # dead_dict = {} ->(뿌리는 r,뿌리는 c):set( (죽는r,죽는c) )
    # matrix 조회
    max_index = (-1, -1)
    max_value = 0
    for row in range(row_num):
        for col in range(row_num):
            if matrix[row][col] <= 0:
                continue
            # 기존 숲 탐색
            dead_dict[(row,col)] = set()
            dead_dict[(row,col)].add((row,col))
            # (기존 숲에 제초제 뿌리면 얼만큼 죽이는지 숫자,- r,- c) > (최댓값,-r,-c) 이면 업데이트
            temp_score = matrix[row][col]
            for dir in range(4,8):
                for step in range(1,spread_size+1):
                    next_r,next_c = row+step*dr[dir],col+step*dc[dir]
                    # 범위밖
                    if not in_range(next_r,next_c):
                        break
                    # 나무가 있는 경우
                    if (matrix[next_r][next_c] > 0):
                        temp_score += matrix[next_r][next_c]
                        dead_dict[(row,col)].add((next_r,next_c))
                    # 빈칸 혹은 벽이 있는 경우
                    else:
                        dead_dict[(row,col)].add((next_r,next_c))
                        break

            if (temp_score,-row,-col) > (max_value,-max_index[0],-max_index[1]):
                max_value = temp_score
                max_index = (row,col)
    if max_value != 0:
        # 그렇게 제일 높은 거 찾았으면 dead_dict활용해서 죽이기
        for (kill_r,kill_c) in dead_dict[max_index]:
            matrix[kill_r][kill_c] = -( remain_dead + 1 )
        score += max_value
    # 4. 벽을 제외하고 음수인 것들 (+1)
    for i in range(row_num):
        for j in range(row_num):
            if (i,j) in wall_set:
                continue
            if matrix[i][j]<0:
                matrix[i][j]+=1


print(score)