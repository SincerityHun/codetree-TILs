import sys

L, Q = map(int,sys.stdin.readline().strip("\n").split())
# L: 자릿수, Q: 명령수
# print(L,Q)
sushi = dict()
people = dict()
people_set = set()
sushi_number = 0
time = 0
for _ in range(Q):
    # print("sushi\n",sushi)
    # print("people\n",people)
    temp_line= sys.stdin.readline().strip("\n").split()

    # 시간 간격 확인
    new_time = int(temp_line[1])
    time_space = new_time - time

    # 매번 명령을 받기 전
    for t in range(time_space):
        for name in sushi.keys():
            temp = {}
            for index in sushi[name].keys():
                temp[(index+1)%L] = sushi[name][index]
            sushi[name] = temp
        # 모든 이름에 대해 자기 자리에 해당하는 초밥을 지우기
        for name in people.keys():
            # 현재 초밥 종류 자리 지우기
            x = people[name][0] # 좌표
            if sushi.get(name):
                if sushi[name].get(x):  # 해당 칸에 한 개라도 이미 있다면
                    people[name][1] -= sushi[name][x]
                    sushi_number -= sushi[name][x]
                    del sushi[name][x]
                    # 만약에 다 먹었어?
                    if people[name][1] == 0:
                        # 사람 뺴고
                        people_set.remove(name)
                        # 스시 뺴고
                        del sushi[name]

    if temp_line[0] == "100": # 스시 넣는 경우
        x = int(temp_line[2])
        name = temp_line[3]
        sushi_number += 1 # 스시 개수 추가
        if sushi.get(name): # 이미 넣은 적 있는 초밥 종류인 경우
            if sushi[name].get(x): # 이미 한 개라도 이 칸에 있어.
                sushi[name][x] += 1
            else: # 아예 없는 칸이야
                sushi[name][x] = 1
        else: # 넣은 적 없는 초밥 종류인 경우
            sushi[name] = {x:1} # 위치:개수

        # 스시 넣은 위치에 사람이 있는지 검사해야지
        if people.get(name):
            if people[name][0] == x:
                # 사람이 먹고
                people[name][1] -= 1
                # 스시는 0으로 만들고
                sushi_number -= 1
                del sushi[name][x]
                #만약에 사람이 다 먹었어?
                if people[name][1] == 0:
                    # 사람 뺴고
                    people_set.remove(name)
                    # 스시 뺴고
                    del sushi[name]

    elif temp_line[0] == "200": # 사람 넣는 경우
        x = int(temp_line[2])
        name = temp_line[3]
        num = int(temp_line[4])

        # 자리에 사람 넣고
        people[name] =[x,num]
        people_set.add(name)

        # 현재 초밥 종류 자리 지우기
        if sushi.get(name):
            if sushi[name].get(x): # 해당 칸에 한 개라도 이미 있다면
                people[name][1] -= sushi[name][x]
                sushi_number -= sushi[name][x]
                del sushi[name][x]
                # 만약에 다 먹었어?
                if people[name][1] == 0:
                    # 사람 뺴고
                    people_set.remove(name)
                    # 스시 뺴고
                    del sushi[name]

    else: # 사진 찍는 경우
        print(len(people_set),sushi_number)

    # 시간 업데이트
    time = new_time
# 초밥 딕셔너리
# 사람 딕셔너리


# 초밥을 넣는 경우
    # 처음 넣는 경우
       # "sam":{"위치":"1"}
    # 이미 있는 경우
        # "sam":{"해당 위치에 있음 넣고 없음 말고":"1추가"}

# 사람을 넣는 경우
    # 처음 넣는 경우
        # "sam":[자리,먹어야되는 초밥 수]
        # 이름 세트에 넣기!
        # 현재 자리에 나의 이름에 해당하는 초밥이 있다면 지우기

# 사진을 찍는 경우
    # 이름 셋 개수,