import sys
from collections import deque

# 1. 정의

weight = {}
set_conveyor = dict() # 상자 ID: 컨베이너 Index
item_conveyor = dict() # 컨베이어 index : deque()
# 2. 입력 받기
q = int(input()) # 질문받기
factory = sys.stdin.readline().rstrip().split()
n = int(factory[1]) # n개의 상자
m = int(factory[2]) # 컨베이너 개수
conveyor_len = n/m

for id_index in range(3,n+3):
    # weight_index = id_index + n
    box_id = int(factory[id_index])
    conveyor_id =int((id_index - 3) // conveyor_len)+1
    box_weight = int(factory[id_index+n])

    # Save Conveyor
    set_conveyor[box_id] = conveyor_id

    # Append
    if item_conveyor.get(conveyor_id) is None:
        item_conveyor[conveyor_id] = deque()
    item_conveyor[conveyor_id].append(box_id)
    weight[box_id] = box_weight # weight update


# factory를 바탕으로 set_conveyor, item_conveyor 채우기
#print(set_conveyor)
# print(item_conveyor)
# 3. 최적화
for _ in range(q-1):
    choice, value = map(int,input().split())
    if choice == 200: # 하차
        result = 0
        for conveyor_id in range(1,m+1):
            # 패쇄된 컨베이어인지 확인
            if item_conveyor[conveyor_id] == -1 or len(item_conveyor[conveyor_id]) == 0:
                continue
            # 아니면 뽑고 진행
            item = item_conveyor[conveyor_id].popleft()
            if weight[item] <= value:
                # 하차
                result += weight[item]
                set_conveyor[item] = -1 # 이제 얘는 없다...
            else:
                # 빽
                item_conveyor[conveyor_id].append(item)
        print(result)
    elif choice == 300:
        if set_conveyor.get(value) is None or set_conveyor[value] == -1:
            # 아예 들어온적 없거나 + 나가서 -1이된 경우
            print(-1)
        else:
            r_conveyor = set_conveyor[value] # 삭제할 상자가 있는 컨베이어 벨트
            item_conveyor[r_conveyor].remove(value)
            set_conveyor[value] = -1 # 나갔음
            print(value)

    elif choice == 400:
        if set_conveyor.get(value) is None or set_conveyor[value] == -1:
            # 아예 들어온적 없거나 + 나가서 -1이된 경우
            print(-1)
        else:
            f_conveyor = set_conveyor[value] # 탐색할 상자가 있는 컨베이어 벨트
            flag = -1
            len_item = len(item_conveyor[f_conveyor]) # 컨베이어 벨트 길이
            for item_index in range(len_item):
                if item_conveyor[f_conveyor][item_index] == value:
                    flag = item_index # 찾았다
                    break
            for item_index in range(0,flag):
                item = item_conveyor[f_conveyor].popleft()
                item_conveyor[f_conveyor].append(item)

            print(f_conveyor)
    else: #벨트 고장
        if item_conveyor[value] == -1:
            print(-1)
        else:
            for index in range(m):
                conveyor_index = ((value + index) % m)+1 # 여기로 옮길거야
                if item_conveyor[conveyor_index] != -1:
                    # value에 있는걸 convayor_index로 옮겨야해
                    item_conveyor[conveyor_index].extend(item_conveyor[value])
                    for item in item_conveyor[value]:
                        set_conveyor[item] = conveyor_index
                    # item 컨테이너 고장 처리
                    item_conveyor[value] = -1
                    print(value)
                    break
                else:
                    continue