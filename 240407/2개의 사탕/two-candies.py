import sys
from collections import deque
N,M = map(int,sys.stdin.readline().rstrip().split())

matrix = []
# O(N * M)
for i in range(N):
    matrix.append(list(sys.stdin.readline().rstrip()))

# O(N*M)
start_blue_index = 0
start_red_index = 0
exit_index = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == "B":
            start_blue_index = (i,j)
            matrix[i][j] = "."
        elif matrix[i][j] == "R":
            start_red_index = (i,j)
            matrix[i][j] = "."
        elif matrix[i][j] == "O":
            exit_index = (i,j)
            matrix[i][j] = "."
class Item:
    def __init__(self,red_r,red_c,blue_r,blue_c,current_count):
        self.red_r = red_r
        self.red_c = red_c
        self.blue_r = blue_r
        self.blue_c = blue_c
        self.current_count = current_count
dir_r = [0,1,0, -1]
dir_c = [1,0,-1,0]
def predict(r,c,dir):
    count = 0
    while matrix[r][c] != "#":
        r += dir_r[dir]
        c += dir_c[dir]
        count += 1
    r -= dir_r[dir]
    c -= dir_c[dir]
    count -= 1
    return (r,c,count)
def bfs():
    # 시작점 deque에 넣어두기
    item_list = deque()
    item_list.append(Item(start_red_index[0],start_red_index[1],start_blue_index[0],start_blue_index[1],0))

    # deque 빌 때까지 for 문 ON
    while len(item_list) != 0:
    # 0. deque popleft
        current_item = item_list.popleft()
    # 1. count 증가 -> 증가했는데 11? Continue
        current_item.current_count = current_item.current_count + 1
        if current_item.current_count == 11:
            continue
    # 2. for 우->하->좌->상
        for i in range(4):
    # 2.1. 빨, 파 위치 예측
            next_red_index = predict(current_item.red_r,current_item.red_c,i)
            next_blue_index = predict(current_item.blue_r,current_item.blue_c,i)
    # 2.2 위치가 같다면 이전 위치를 기준으로 더 가까운 쪽이 가지고 아닌 쪽은 한칸 아닌 쪽으로 이동
            if (next_red_index[0],next_red_index[1]) != exit_index and (next_blue_index[0],next_blue_index[1]) != exit_index:
                if next_red_index[0] == next_blue_index[0] and next_red_index[1] == next_blue_index[1]:
                    if next_red_index[2] > next_blue_index[2]:
                        next_red_index = (next_red_index[0]-dir_r[i], next_red_index[1]-dir_c[i],next_red_index[2]-1)
                    elif next_red_index[2] < next_blue_index[2]:
                        next_blue_index = (next_blue_index[0]-dir_r[i], next_blue_index[1]-dir_c[i],next_blue_index[2]-1)
    # 2.3 파가 Exit 위치인지 확인 -> Exit이면 Continue
            if (next_blue_index[0],next_blue_index[1]) == exit_index:
                continue
    # 2.4. 빨이 Exit 위치인지 확인 -> 걍 이떄 count값 return
            if (next_red_index[0],next_red_index[1]) == exit_index:
                return current_item.current_count
    # 2.5. deque append
            item_list.append(Item(next_red_index[0],next_red_index[1],next_blue_index[0],next_blue_index[1],current_item.current_count))
    return -1
print(bfs())