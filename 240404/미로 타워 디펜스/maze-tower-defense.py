# Linked List
import sys
from collections import defaultdict

# n: n*n 배열, 최대 몬스터 개수: n*n - 1,
# m: 라운드 수
n,m = map(int,sys.stdin.readline().rstrip().split())
max_monster_num = n*n - 1
global_monster_num = 0 # 지금까지 들어온 몬스터 수, 즉 새로 추가할때, 이거 1로 늘리고 데이터를 계속 넣으면 된다. ID관리용
# 새로 넣기 전에 current_monster_num이 이미 max_monster_num과 같다면, 더이상 추가 불가.
current_monster_num = 0 # 현재 남아있는 몬스터 수, 새로 추가할때, 이것도 같이 늘려줘야함. 단, 죽으면 이건 지워줘야 된다.
total_score = 0 # 전체 점수

# 일단 2중 배열 받기 O(n)
temp_map = [[0]*n for _ in range(n)]
for i in range(n):
    temp_map[i] = sys.stdin.readline().rstrip().split() # str로 들어갔다!


# 받은 2중 배열 Double Linked List 에 연결하기
data_dict = dict()
next_dict = dict()
before_dict = dict()

data_dict[0] = "HEAD"
data_dict[-1] = "TAIL"
next_dict[0] = -1
next_dict[-1] = None
before_dict[0] = None
before_dict[-1] = 0

# 이게 True면 더 넣을 수 있다.
def check_len_of_list():
    if current_monster_num == max_monster_num:
        return False
    return True

# Doubled Linked List add
def add_item_in_double_linked_list(value:int,before_ID):
    global global_monster_num,current_monster_num
    if check_len_of_list() == False:
        return

    global_monster_num += 1
    current_monster_num += 1
    # data_dict에 값 넣기
    data_dict[global_monster_num] = value
    # 기존 꺼 확인
    next_ID = next_dict[before_ID]
    # next_dict 수정하기
    next_dict[before_ID] = global_monster_num
    next_dict[global_monster_num] = next_ID
    # before_dict 수정하기
    before_dict[global_monster_num] = before_ID
    before_dict[next_ID] = global_monster_num

# item 별로 삭제
def delete_item_in_double_linked_list(target_ID):
    global next_dict
    global before_dict
    global current_monster_num
    before_ID = before_dict[target_ID]
    next_ID = next_dict[target_ID]
    # before_ID의 next을 next_ID로 바꿔주고
    next_dict[before_ID] = next_ID
    # next ID의 before을 before_ID로 바꿔주면 된다.
    before_dict[next_ID] = before_ID
    # current 감소!
    current_monster_num -= 1
    return data_dict[target_ID]
# 범위 별로 삭제
# map에서 더블링크드리스트로 전환
def add_item_from_map():
    current_index = (n//2,n//2 - 1)
    flag = False
    history_step = 1 # 최대치
    step = 0 # 현재 단계에서 진행중인 개수
    move_flag = 0 # 현재 진행중인 move
    move = [(0,-1),(1,0),(0,1),(-1,0)]
    while temp_map[current_index[0]][current_index[1]] != '0' and check_len_of_list():
        # 일단 넣어
        add_item_in_double_linked_list(int(temp_map[current_index[0]][current_index[1]]),global_monster_num)
        # 넣고 step update
        # 현재 step이 남아있어?
        if step == 0:
            # flag가 True면 최대치 1증가하고 false
            if flag:
                history_step += 1
                flag = False
            # flag가 False면 flag True
            else:
                flag = True
            # move_flag 증가
            move_flag = (move_flag +1) % 4
            # step 을 최대치고
            step = history_step

        # index 이동
        # move_flag에 해당하는 move을 하고 step 감소
        current_index = (current_index[0] + move[move_flag][0], current_index[1] + move[move_flag][1])
        step -= 1

# 더블링크드 리스트 출력
def print_item_in_double_linked_list():
    start_index = 0
    while next_dict[start_index] != None:
        print(data_dict[start_index],end=" ")
        start_index = next_dict[start_index]
    print()

# map -> double linked list
add_item_from_map()
# print_item_in_double_linked_list() # TEST
memo = dict()
def cal_index(d,k):
    global memo
    index = 0
    if memo.get(k):
        index += memo[k]
    else:
        for x in range(1,k):
            index += 8*x
        memo[k] = index
    if d == 0: # 우
        index += 5*k
    elif d == 1: # 하
        index += 3 * k
    elif d == 2: # 좌
        index += k
    else: # 상
        index += 7*k

    return index
def attack(d,p): # d: 방향, p: 몇칸
    check_set = set()
    for i in range(1,p+1):
        # index를 계산
        index = cal_index(d,i)
        # 계산한 index를 check_set에 넣기
        check_set.add(index)

    # check_set에 있는 index일때마다 값 가져오기 + 뺴야함
    result = 0
    pointer = next_dict[0]
    step = 1
    while pointer != -1:
        # check_set이 비었으면 아웃
        if len(check_set) == 0:
            break
        # 그 다음꺼 미리 받고
        next_ID = next_dict[pointer]
        # 현재 스텝이 포함되는 지 확인
        if step in check_set:
            check_set.remove(step)
            result += delete_item_in_double_linked_list(pointer)
        # 칸 이동
        step += 1
        pointer = next_ID
    return result

def delete_range_item(start_id,end_id):
    before_start_id = before_dict[start_id]
    next_end_id = next_dict[end_id]
    # 처음꺼의 이전꺼를 마지막꺼로 이으면 되지 않나?
    next_dict[before_start_id] = next_end_id
    before_dict[next_end_id] = before_start_id

def check_duplicated_item(standard):
    item = [] # (시작 ID, 끝 ID, 총 개수, 값)
    pointing_ID = next_dict[0]
    current_flag = data_dict[pointing_ID] # 값
    start_id = pointing_ID
    end_id = pointing_ID
    duplicated_count = 0
    while pointing_ID != -1:
        temp_data = data_dict[pointing_ID]
        if current_flag == temp_data:
            duplicated_count += 1
            end_id = pointing_ID

        else:
            if duplicated_count >= standard :
                item.append((start_id,end_id,duplicated_count,current_flag))
            duplicated_count = 1
            start_id = pointing_ID
            end_id = pointing_ID
            current_flag = temp_data

        pointing_ID = next_dict[pointing_ID]
    # 마지막 한개일경우
    if duplicated_count >= standard:
        item.append((start_id, end_id, duplicated_count, current_flag))
    return item

def delete_duplicate():
    global current_monster_num
    result = 0
    while True:
        item_list = check_duplicated_item(4)
        if len(item_list) == 0:
            break

        for item in item_list:
            result += item[2] * item[3]
            delete_range_item(item[0],item[1])
            current_monster_num -= item[2]
    return result

def update_list():
    global current_monster_num
    # 중복 확인
    item_list = check_duplicated_item(1)
    # print("ITEM LIST")
    # print(item_list)
    for item in item_list:
        # print("ITEM: ",item)
        # print_item_in_double_linked_list()
        start_id,end_id,duplicated_count,current_flag = item
        before_start_id = before_dict[start_id]
        # 제거
        delete_range_item(start_id,end_id)
        current_monster_num -= duplicated_count
        # 삽입
        add_item_in_double_linked_list(duplicated_count, before_start_id)
        duplicate_count_id = next_dict[before_start_id]
        add_item_in_double_linked_list(current_flag,duplicate_count_id)

# print_item_in_double_linked_list()

for _ in range(m):
    d,p = map(int,sys.stdin.readline().rstrip().split())
    # 1 공격
    total_score += attack(d,p)
    # print("AFTER ATTACK")
    # print_item_in_double_linked_list()
    # 3. 4번 이상 반복해 나오면 해당 몬스터 또한 삭제
    total_score += delete_duplicate()
    # print("AFTER DELETE")
    # print_item_in_double_linked_list()
    # 4. 연속해서 같은 숫자 -> (연속한 총개수, 숫자 크기) 로 치환
    update_list()
    # print("AFTER UPDATE")
    # print_item_in_double_linked_list() # TEST
    # print(total_score) # TEST

print(total_score)