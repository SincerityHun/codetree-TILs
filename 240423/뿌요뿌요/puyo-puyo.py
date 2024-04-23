# 터지게 되는 블럭
# 최대 블럭의 크기
from collections import deque
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

global_visited = set()
def in_range(r,c):
    return (0<=r<N) and (0<=c<N)
dr = [-1,0,1,0]
dc = [0,1,0,-1]
result_dict = dict()
for global_r in range(N):
    for global_c in range(N):
        if not in_range(global_r,global_c):
            continue
        if (global_r,global_c) in global_visited:
            continue
        start_index = (global_r,global_c)
        start_value = matrix[global_r][global_c] # 값
        result_dict[start_index] = 1 # 블럭수
        local_visited = set()
        local_visited.add(start_index)
        bfs_queue = deque([start_index])
        while len(bfs_queue) != 0:
            cur_r, cur_c = bfs_queue.popleft()
            for i in range(4):
                next_r,next_c = cur_r+dr[i],cur_c+dc[i]
                if not in_range(next_r,next_c):
                    continue
                if (next_r,next_c) in local_visited:
                    continue
                if matrix[next_r][next_c] != start_value:
                    continue
                local_visited.add((next_r,next_c))
                bfs_queue.append((next_r,next_c))
                result_dict[start_index] += 1
        global_visited.update(local_visited)
print(len([x for x in result_dict.values() if x >= 4]),max(list(result_dict.values())))