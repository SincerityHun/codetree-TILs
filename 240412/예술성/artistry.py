# N*N 격자
# 각 칸 1 ~ 10
# 동일 숫자 동일 그룹
# 각 그룹의 조화 = (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
# 0보다 큰 조화로움의 그룹 쌍 합 => 초기 예술 점수
# 그림의 회전 진행
# 십자모양 -> 반시계 90도
# 4개의 정사각형 -> 시계 90도
# 돌고나서 예술 점수 구함
# 1,2,3회전 후 예술 점수의 합 구하기
from collections import deque

row_num = int(input())
matrix = []  # 초기, 1회전,2회전,3회전
for i in range(row_num):
    matrix.append(list(map(int, input().split())))
# 회전 결과 구하기 상,우,하,좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
score = 0
temp_metrix = [[0]*row_num for i in range(row_num)]
start_index = [(0,0),(0,row_num//2+1),(row_num//2 + 1,0),(row_num//2+1, row_num//2 + 1)]
# 범위 확인
def in_range(r,c):
    return (0<=r<row_num) and (0<=c<row_num)
for time in range(4):
    # 그룹을 구하고
    cur_group_num = 0  # 현재 카운팅 되고 있는 유효한 그룹 개수
    group_dict = dict()  # cur_group_id : set((r,c)) 속하는 것들
    other_dict = dict()  # cur_group_id : set((r,c)) 맡닿은 것들
    visited = set()
    for i in range(row_num):
        for j in range(row_num):
            if (i, j) in visited:
                continue
            # 새로운 그룹의 시작
            cur_group_num += 1
            criteria = matrix[i][j]
            group_dict[cur_group_num] = set()
            other_dict[cur_group_num] = list()
            group_dict[cur_group_num].add((i,j))
            temp_visited = {(i,j)}
            bfs_queue = deque([(i, j)])
            while len(bfs_queue) != 0:
                cur_r, cur_c = bfs_queue.popleft()
                for dir in range(4):
                    next_r,next_c = cur_r+dr[dir],cur_c+dc[dir]
                    if ((next_r,next_c) in temp_visited) or (not in_range(next_r,next_c)):
                        continue
                    if matrix[next_r][next_c] == criteria:
                        temp_visited.add((next_r,next_c))
                        bfs_queue.append((next_r,next_c))
                        group_dict[cur_group_num].add((next_r,next_c))
                    else:
                        other_dict[cur_group_num].append((next_r,next_c))
            # 그룹 재정리
            visited.update(temp_visited)
    # 예술 점수 계산
    for cur_group_id in range(1,cur_group_num+1):
        a_index = list(group_dict[cur_group_id])[0]
        a_num = len(group_dict[cur_group_id])
        a = matrix[a_index[0]][a_index[1]]
        for next_group_id in range(cur_group_id+1,cur_group_num+1):
            with_num = 0
            for item in other_dict[cur_group_id]:
                if item in group_dict[next_group_id]:
                    with_num += 1
            if with_num != 0:
                b_index = list(group_dict[next_group_id])[0]
                b_num = len(group_dict[next_group_id])
                b = matrix[b_index[0]][b_index[1]]
                score += ((a_num + b_num)*a*b*with_num)
    # 회전
    # 십자가
    dest_r = row_num//2
    for dest_c in range(0,row_num):
        temp_metrix[row_num - dest_c - 1][row_num//2] = matrix[dest_r][dest_c]
    dest_c = row_num//2
    for dest_r in range(0,row_num):
        temp_metrix[dest_c][dest_r]= matrix[dest_r][dest_c]

    for i in range(row_num//2):
        matrix[i][row_num//2] = temp_metrix[i][row_num//2]
    for j in range(row_num):
        matrix[row_num//2][j] = temp_metrix[row_num//2][j]
    for i in range(row_num//2+1,row_num):
        matrix[i][row_num//2] = temp_metrix[i][row_num//2]


    # 4개의 정사각형
    for (start_r,start_c) in start_index:
        for r in range(start_r,start_r + row_num//2): # 0,1
            for c in range(start_c,start_c + row_num//2):# 3,4
                temp_metrix[c-start_c][(row_num//2 - 1) - (r-start_r)] = matrix[r][c]
        for r in range(start_r,start_r + row_num//2):
            for c in range(start_c,start_c+row_num//2):
                matrix[r][c] = temp_metrix[r-start_r][c-start_c]

print(score)