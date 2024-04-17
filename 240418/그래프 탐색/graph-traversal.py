from collections import defaultdict
N,M = map(int,input().split()) # N개의 정점, M개의 간선

tree_dict = defaultdict(set)

for i in range(M):
    a,b = map(int, input().split())
    tree_dict[a].add(b)
    tree_dict[b].add(a)

visited = set()
visited.add(1)
def dfs(cur_node):
    get_next_node = tree_dict[cur_node]
    for node in get_next_node:
        if node in visited:
            continue
        visited.add(node)
        dfs(node)

dfs(1)
visited.remove(1)
print(len(visited))