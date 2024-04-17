n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split()))) 

start_index = (0,0)
dr = [1,0]
dc = [0,1]

visited = set()
visited.add(start_index)
def in_range(cur_r,cur_c):
    return (0<=cur_r<n)and(0<=cur_c<n)
def dfs(cur_node):
    cur_r, cur_c = cur_node
    if (cur_r,cur_c) == (n-1,m-1):
        return True
    for i in range(2):
        next_r,next_c = cur_r+dr[i], cur_c+dc[i]
        if (next_r,next_c) in visited or not in_range(next_r,next_c):
            continue
        if matrix[next_r][next_c] == 0:
            continue
        visited.add((next_r,next_c))
        return dfs((next_r,next_c))
    return False

if dfs(start_index):
    print(1)
else:
    print(0)