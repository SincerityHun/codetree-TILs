import sys
from collections import deque
N,team_num,round_num = map(int,sys.stdin.readline().strip().split())
# 전체 맵 받기 O(N)
matrix = []
for i in range(N):
    matrix.append(list(map(int,sys.stdin.readline().rstrip().split())))
# 전체 맵에서 Head, Tail을 팀 최대 개수를 기준으로 각각 받기
HEAD = dict()
TAIL = dict()
team_index = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            HEAD[team_index] = (i,j)
            team_index += 1

# 우, 하, 좌, 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def check_range(r,c):
    return 0<=r<N and 0<=c<N
def find_next_for_tail(r,c):
    for dir in range(4):
        if check_range(r+dr[dir],c+dc[dir]):
            if matrix[r+dr[dir]][c+dc[dir]] in (2,3):
                return (r+dr[dir],c+dc[dir])
    return False

def find_tail(team):
    current_index = HEAD[team]
    # current_index가 3이 될때까지 이동 후 찾기
    while matrix[current_index[0]][current_index[1]] != 3 :
        current_index = find_next_for_tail(current_index[0],current_index[1])
    # 그 인덱스 반환
    return current_index
for head_index in range(team_num):
    TAIL[head_index] = find_tail(head_index)

# print(HEAD)
# print(TAIL)
def find_next_specific_value(r,c,value):
    for dir in range(4):
        if check_range(r+dr[dir],c+dc[dir]):
            if matrix[r+dr[dir]][c+dc[dir]] == value:
                return (r+dr[dir],c+dc[dir])
    return False
def move():
    for team in range(team_num):
        # 바로 있을 경우 생략해쌎ㅎ아 어씨발
        next_head = find_next_specific_value(HEAD[team][0],HEAD[team][1],4)
        next_tail = find_next_specific_value(TAIL[team][0],TAIL[team][1],2)
        if next_head == False:
            next_head = TAIL[team]
        # 바로 붙어있을 경우, tail은 2를 평생 못찾지?
        if next_tail == False:
            next_tail = HEAD[team]
        # head 의 값은 2로 , 그 옆의 건 4는 1로
        # tail 의 값은 4로 , 그 옆의 거 2는 3으로
        matrix[HEAD[team][0]][HEAD[team][1]] = 2
        matrix[TAIL[team][0]][TAIL[team][1]] = 4
        HEAD[team] = next_head
        TAIL[team] = next_tail
        matrix[HEAD[team][0]][HEAD[team][1]] = 1
        matrix[TAIL[team][0]][TAIL[team][1]] = 3

def find_hit_index(round):
    way = ((round-1)//(N)) %4 # 0, 1, 2,3 우로,위로,좌로,아래로
    count = (round+N-1) % N  # 0,,,,N-1
    if way == 0:
        return (count,0,way)
    elif way == 1:
        return (N-1,count,way)
    elif way == 2:
        return (N-1 - count , N-1,way)
    else:
        return(0, N-1-count,way)
score = 0
def bfs(index):
    visited = set()
    visited.add(index)
    next_list = deque()
    count = 1
    next_list.append((index,count))
    head = 0
    tail = 0
    if matrix[index[0]][index[1]] == 1:
        head = (index, 1)
        return head
    while len(next_list) != 0:
        next_index,current_count = next_list.popleft()
        for i in range(4):
            next_pointer = (next_index[0]+dr[i],next_index[1]+dc[i])
            if next_pointer in visited or check_range(next_pointer[0],next_pointer[1]) == False:
                continue
            if matrix[next_pointer[0]][next_pointer[1]] == 2:
                next_list.append((next_pointer,current_count+1))
            elif matrix[next_pointer[0]][next_pointer[1]] == 1:
                head =(next_pointer,current_count+1)
            visited.add(next_pointer)
    return head


def get_score(hit_index):
    global HEAD, TAIL
    # 처음 맞은 사람 => 1,2,3찾기
    pointer = 0
    if hit_index[2] == 0:
        for i in range(N):
            if matrix[hit_index[0]][hit_index[1]+i] in (1,2,3):
                pointer = (hit_index[0],hit_index[1]+i)
                break
    elif hit_index[2] == 1:
        for i in range(N):
            if matrix[hit_index[0]-i][hit_index[1]] in (1,2,3):
                pointer = (hit_index[0]-i,hit_index[1])
                break
    elif hit_index[2] == 2:
        for i in range(N):
            if matrix[hit_index[0]][hit_index[1]-i] in (1,2,3):
                pointer = (hit_index[0],hit_index[1]-i)
                break
    else:
        for i in range(N):
            if matrix[hit_index[0]+i][hit_index[1]] in (1,2,3):
                pointer = (hit_index[0]+i,hit_index[1])
                break
    # 없으면 0점 반환
    if pointer == 0:
        return 0
    # 1까지의 거리 찾고 점수 반환하기
    head = bfs(pointer)
    result = head[1]**2
    # 해당 꼬리 머리 바꾸기
    for i in range(team_num):
        if HEAD[i]==head[0]:
            HEAD[i] = TAIL[i]
            TAIL[i] = head[0]
            break
    return result

for i in range(round_num):
    # 1. 한칸 이동
    move()
    # 2. 공 쏘고 맞춘 사람 위치 찾기
    get_hit_index = find_hit_index(i+1)

    # 3. 위치가 있다면, 몇번쨰 사람인지 찾아서
        #3.1 점수 계산
        #3.2 머리사람과 꼬리사람 바꾸기
    score += get_score(get_hit_index)
    # 4. 위치가 없다면 그다음 라운드 시작
print(score)