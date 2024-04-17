from collections import deque

row_num, col_num = map(int,input().split())
matrix = []
for _ in range(row_num):
    matrix.append(list(map(int,input().split())))

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def in_range(r,c):
    return (0<=r<row_num) and(0<=c<col_num)
# K 설정
def bfs(k):
    global_visited = set()
    result = 0
    for row in range(row_num):
        for col in range(col_num):
            if (row,col) in global_visited or matrix[row][col] <= k:
                continue
            start_index = (row,col)
            result += 1
            visited = set()
            visited.add(start_index)
            bfs_queue = deque([start_index])
            while len(bfs_queue) != 0:
                cur_r,cur_c = bfs_queue.popleft()
                for dir in range(4):
                    next_r,next_c = cur_r+dr[dir],cur_c+dc[dir]
                    if not in_range(next_r,next_c) or (next_r,next_c) in visited:
                        continue
                    if matrix[next_r][next_c] <= k:
                        continue
                    visited.add((next_r,next_c))
                    bfs_queue.append((next_r,next_c))
            global_visited.update(visited)
    return result
count = 0
max_k = 1
for k in range(1,max([max(row) for row in matrix])+1):
    result = bfs(k)
    if count < result:
        max_k=k
        count = result
print(max_k,count)