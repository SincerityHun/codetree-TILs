# 4*4 격자
# 상, 하, 좌, 우 정하면 모든 숫자가 그 방향으로 밀림
# 같은 숫자가 민나면 합쳐짐
# 연쇄에 연쇄는 안일어남
# 서너개가 합쳐질 수는 없고, 바닥에서 가까운 순서대로 한쌍 씩 짝을 이뤄 합쳐짐
# 2, 4, 8, 16,,,만 잇음
# 5번 움직인 이후에 격자판에서 가장 큰 값의 최댓값을 구하는 프로그램
# 5번을 어떻게 움직일지는 자유 -> 4*4*4*4*4

row_num = int(input())

start_matrix =[]
for i in range(row_num):
    start_matrix.append(list(map(int,input().split())))
# 위, 아래, 왼쪽, 오른쪽
max_value = 0
def in_range(r,c):
    return (0<=r<row_num) and (0<=c<row_num)
def get_turn(matrix,dir,count):
    global max_value
    # dir방향으로 matrix을 돌림
    if dir == 0:
        # column고정 row이동
        start_r= 0
        start_c,end_c = 0,row_num-1
        for cur_c in range(start_c,end_c+1):
            a_point = (start_r,cur_c)
            b_point = (start_r+1,cur_c)
            # b_point 범위 안이면 while
            while(in_range(b_point[0],b_point[1])):
                a_value = matrix[a_point[0]][a_point[1]]
                b_value = matrix[b_point[0]][b_point[1]]
                # a_point가 빈칸이면 a랑 b둘다 옮겨야됨
                if a_value == 0:
                    while in_range(b_point[0],b_point[1]) and matrix[b_point[0]][b_point[1]] == 0:
                        b_point = (b_point[0]+1,b_point[1])

                    if in_range(b_point[0],b_point[1]):
                        matrix[a_point[0]][a_point[1]] =  matrix[b_point[0]][b_point[1]]
                        matrix[b_point[0]][b_point[1]] = 0
                        a_point = (a_point[0]+1,a_point[1])
                        b_point = (a_point[0]+1,a_point[1])
                    continue
                # b_point가 빈칸이면 다음칸 슛
                if b_value == 0:
                    b_point = (b_point[0]+1,b_point[1])
                    continue
                # b_point가 a_point와 같은 값이라면?
                if a_value == b_value:
                    # a_point자리에 둘이 값 합한 거 넣고
                    matrix[a_point[0]][a_point[1]] = a_value + b_value
                    # b_point자리에 0 넣고
                    matrix[b_point[0]][b_point[1]] = 0
                    # a_point는 a_point 한칸 뒤로
                    a_point = b_point
                    # b_point는 a point 한칸 뒤로
                    b_point = (a_point[0]+1,a_point[1])
                # b_point가 a_point와 다른 값이라면?
                else:
                    # a_point 한칸 앞
                    a_point = (a_point[0]+1,a_point[1])
                    # a_point 자리에 b_point 값넣고
                    matrix[a_point[0]][a_point[1]] = b_value
                    # b_point자리에 0 두고
                    if a_point != b_point:
                        matrix[b_point[0]][b_point[1]] = 0
                    # a_point 바로 앞에 자리에 b_point 옮기기
                    b_point = (a_point[0]+1,a_point[1])
    elif dir == 1:
        # row고정 column 이동
        start_r,end_r = 0,row_num-1
        start_c = row_num-1
        for cur_r in range(start_r,end_r+1):
            a_point = (cur_r,start_c)
            b_point = (cur_r,start_c-1)
            # b_point 범위 안이면 while
            while(in_range(b_point[0],b_point[1])):
                a_value = matrix[a_point[0]][a_point[1]]
                b_value = matrix[b_point[0]][b_point[1]]
                # a_point가 빈칸이면 a랑 b둘다 옮겨야됨
                if a_value == 0:
                    while in_range(b_point[0],b_point[1]) and matrix[b_point[0]][b_point[1]] == 0:
                        b_point = (b_point[0],b_point[1]-1)
                    if in_range(b_point[0],b_point[1]):
                        matrix[a_point[0]][a_point[1]] = matrix[b_point[0]][b_point[1]]
                        matrix[b_point[0]][b_point[1]] = 0
                        a_point = (a_point[0],a_point[1]-1)
                        b_point = (a_point[0],a_point[1]-1)
                    continue
                # b_point가 빈칸이면 다음칸 슛
                if b_value == 0:
                    b_point = (b_point[0],b_point[1]-1)
                    continue
                # b_point가 a_point와 같은 값이라면?
                if a_value == b_value:
                    # a_point자리에 둘이 값 합한 거 넣고
                    matrix[a_point[0]][a_point[1]] = a_value + b_value
                    # b_point자리에 0 넣고
                    matrix[b_point[0]][b_point[1]] = 0
                    # a_point는 a_point 한칸 뒤로
                    a_point = b_point
                    # b_point는 a point 한칸 뒤로
                    b_point = (a_point[0],a_point[1]-1)
                # b_point가 a_point와 다른 값이라면?
                else:
                    # a_point 한칸 앞
                    a_point = (a_point[0],a_point[1]-1)
                    # a_point 자리에 b_point 값넣고
                    matrix[a_point[0]][a_point[1]] = b_value
                    # b_point자리에 0 두고
                    if a_point != b_point:
                        matrix[b_point[0]][b_point[1]] = 0
                    # a_point 바로 앞에 자리에 b_point 옮기기
                    b_point = (a_point[0],a_point[1]-1)
    elif dir == 2:
        # col 고정 row 이동
        start_r,end_r = row_num-1,0
        start_c,end_c = 0,row_num-1
        for cur_c in range(start_c,end_c+1):
            a_point = (start_r,cur_c)
            b_point = (start_r-1,cur_c)
            # b_point 범위 안이면 while
            while(in_range(b_point[0],b_point[1])):
                a_value = matrix[a_point[0]][a_point[1]]
                b_value = matrix[b_point[0]][b_point[1]]
                # a_point가 빈칸이면 a랑 b둘다 옮겨야됨
                if a_value == 0:
                    while in_range(b_point[0],b_point[1]) and matrix[b_point[0]][b_point[1]] == 0:
                        b_point = (b_point[0]-1,b_point[1])
                    if in_range(b_point[0],b_point[1]):
                        matrix[a_point[0]][a_point[1]] = matrix[b_point[0]][b_point[1]]
                        matrix[b_point[0]][b_point[1]] = 0
                        a_point = (a_point[0]-1,a_point[1])
                        b_point = (a_point[0]-1,a_point[1])
                    continue
                # b_point가 빈칸이면 다음칸 슛
                if b_value == 0:
                    b_point = (b_point[0]-1,b_point[1])
                    continue
                # b_point가 a_point와 같은 값이라면?
                if a_value == b_value:
                    # a_point자리에 둘이 값 합한 거 넣고
                    matrix[a_point[0]][a_point[1]] = a_value + b_value
                    # b_point자리에 0 넣고
                    matrix[b_point[0]][b_point[1]] = 0
                    # a_point는 a_point 한칸 뒤로
                    a_point = b_point
                    # b_point는 a point 한칸 뒤로
                    b_point = (a_point[0]-1,a_point[1])
                # b_point가 a_point와 다른 값이라면?
                else:
                    # a_point 한칸 앞
                    a_point = (a_point[0]-1,a_point[1])
                    # a_point 자리에 b_point 값넣고
                    matrix[a_point[0]][a_point[1]] = b_value
                    # b_point자리에 0 두고
                    if a_point != b_point:
                        matrix[b_point[0]][b_point[1]] = 0
                    # a_point 바로 앞에 자리에 b_point 옮기기
                    b_point = (a_point[0]-1,a_point[1])
    else:
        # row 고정, col 이동
        start_r,end_r = 0,row_num-1
        start_c = 0
        for cur_r in range(start_r,end_r+1):
            a_point = (cur_r,start_c)
            b_point = (cur_r,start_c+1)
            # b_point 범위 안이면 while
            while(in_range(b_point[0],b_point[1])):
                a_value = matrix[a_point[0]][a_point[1]]
                b_value = matrix[b_point[0]][b_point[1]]
                # a_point가 빈칸이면 a랑 b둘다 옮겨야됨
                if a_value == 0:
                    while in_range(b_point[0],b_point[1]) and matrix[b_point[0]][b_point[1]] == 0:
                        b_point = (b_point[0],b_point[1]+1)
                    if in_range(b_point[0],b_point[1]):
                        matrix[a_point[0]][a_point[1]] = matrix[b_point[0]][b_point[1]]
                        matrix[b_point[0]][b_point[1]] = 0
                        a_point = (a_point[0],a_point[1]+1)
                        b_point = (a_point[0],a_point[1]+1)
                    continue
                # b_point가 빈칸이면 다음칸 슛
                if b_value == 0:
                    b_point = (b_point[0],b_point[1]+1)
                    continue
                # b_point가 a_point와 같은 값이라면?
                if a_value == b_value:
                    # a_point자리에 둘이 값 합한 거 넣고
                    matrix[a_point[0]][a_point[1]] = a_value + b_value
                    # b_point자리에 0 넣고
                    matrix[b_point[0]][b_point[1]] = 0
                    # a_point는 a_point 한칸 뒤로
                    a_point = b_point
                    # b_point는 a point 한칸 뒤로
                    b_point = (a_point[0],a_point[1]+1)
                # b_point가 a_point와 다른 값이라면?
                else:
                    # a_point 한칸 앞
                    a_point = (a_point[0],a_point[1]+1)
                    # a_point 자리에 b_point 값넣고
                    matrix[a_point[0]][a_point[1]] = b_value
                    # b_point자리에 0 두고
                    if a_point != b_point:
                        matrix[b_point[0]][b_point[1]] = 0
                    # a_point 바로 앞에 자리에 b_point 옮기기
                    b_point = (a_point[0],a_point[1]+1)
    # count 감소
    count -= 1
    # 감소한게 0이면 matrix의 value중 최댓값이랑 max_value랑 비교해서 업데이트
    if count == 0:
        value = max(max(matrix))
        if  value > max_value:
            max_value = value
    # 감소한게 0이 아니면, 해당 matrix로 dir:0,1,2,3으로 count그대로 보낸다
    else:
        get_turn(matrix,0,count)
        get_turn(matrix,1,count)
        get_turn(matrix,2,count)
        get_turn(matrix,3,count)

get_turn(start_matrix,0,5)
get_turn(start_matrix,1,5)
get_turn(start_matrix,2,5)
get_turn(start_matrix,3,5)

print(max_value)