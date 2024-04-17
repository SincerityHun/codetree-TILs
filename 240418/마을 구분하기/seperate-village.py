from collections import deque

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))


town = []
global_visited = set()
def in_range(r,c):
    return (0<=r<N) and (0<=c<N)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

for i in range(N):
    for j in range(N):
        if ((i,j) in global_visited)or (matrix[i][j] == 0):
            continue
        start_index = (i,j)
        local_num = 0
        visited = set()
        visited.add(start_index)
        bfs_queue = deque([start_index])
        while len(bfs_queue) != 0:
            cur_r,cur_c = bfs_queue.popleft()
            local_num += 1
            for dir in range(4):
                next_r,next_c = cur_r+dr[dir],cur_c+dc[dir]
                if (not in_range(next_r,next_c)) or (next_r,next_c) in visited:
                    continue
                if matrix[next_r][next_c] == 0:
                    continue
                visited.add((next_r,next_c))
                bfs_queue.append((next_r,next_c))

        global_visited.update(visited)
        town.append(local_num)

town.sort()
print(len(town))
for num in town:
    print(num)