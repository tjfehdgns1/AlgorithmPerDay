'''공원 산책
문제 설명
지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 
산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

["방향 거리", "방향 거리" … ]
예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 
로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 
공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 
로봇 강아지가 모든 명령을 수행 후 놓인 위치를 
[세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ park의 길이 ≤ 50
3 ≤ park[i]의 길이 ≤ 50
park[i]는 다음 문자들로 이루어져 있으며 시작지점은 하나만 주어집니다.
S : 시작 지점
O : 이동 가능한 통로
X : 장애물
park는 직사각형 모양입니다.
1 ≤ routes의 길이 ≤ 50
routes의 각 원소는 로봇 강아지가 수행할 명령어를 나타냅니다.
로봇 강아지는 routes의 첫 번째 원소부터 순서대로 명령을 수행합니다.
routes의 원소는 "op n"과 같은 구조로 이루어져 있으며, op는 이동할 방향, n은 이동할 칸의 수를 의미합니다.
op는 다음 네 가지중 하나로 이루어져 있습니다.
N : 북쪽으로 주어진 칸만큼 이동합니다.
S : 남쪽으로 주어진 칸만큼 이동합니다.
W : 서쪽으로 주어진 칸만큼 이동합니다.
E : 동쪽으로 주어진 칸만큼 이동합니다.
1 ≤ n ≤ 9
입출력 예
park	                     routes	                result
["SOO","OOO","OOO"]	        ["E 2","S 2","W 1"]	    [2,1]
["SOO","OXX","OOO"]	        ["E 2","S 2","W 1"] 	[0,1]
["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"] 	[0,0]'''

def solution(park, routes):
    max_x = len(park)
    max_y = len(park[0])
    position = [0,0]
    four_directions = {
        'N' : [-1,0],
        'S' : [1,0],
        'E' : [0,1],
        'W' : [0,-1],
    }

    #시작 지점 찾기
    for index, p in enumerate(park):
        if 'S' in p:
            position[0] = park[index].index('S')
            position[1] = index

    # 위치 이동
    #! 조건문 작성이 잘못되었음
    for route in routes:
        direction, num = route.split()
        num = int(num)

        if position[0] + four_directions[direction][0] * num < max_x or position[1] + four_directions[direction][1] * num < max_y:
            position[0] += four_directions[direction][0] * num
            position[1] += four_directions[direction][1] * num
    return position # 20min, 실패
#################################
def solution(park, routes):
    max_x = len(park[0])
    max_y = len(park)
    position = [0,0]
    directions = {
        'N' : [-1,0],
        'S' : [1,0],
        'E' : [0,1],
        'W' : [0,-1],
    }
    # 시작 지점 찾기
    for y, column in enumerate(park):
        if 'S' in column:
            position = [y, column.index('S')]
            break
    
    # 위치 이동
    for route in routes:
        direction, num = route.split()
        num = int(num)
        step_x = position[1]
        step_y = position[0]
        block = False
        for i in range(num):
            step_x += directions[direction][1]
            step_y += directions[direction][0]
            if step_x <= -1 or step_x >= max_x or step_y <= -1 or step_y >= max_y or park[step_y][step_x] == 'X':
                # 이동할 수 없는 경우
                block = True
                break
        if not block:
            position = [step_y*num, step_x*num]
    return position # 안됨
###############################
def solution(park, routes):
    h = len(park)
    w = len(park[0])
    x,y = 0,0
    
    nav = {
        'S': [1,0],
        'N':[-1,0],
        'W': [0,-1],
        'E':[0,1]
    }
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i
                y = j
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        step_x = x
        step_y = y
        for i in range(1,distance+1):
            step_x += nav[direction][0]
            step_y += nav[direction][1]
            
            if step_x >= h or step_x <= -1 or step_y >= w or step_y <= -1 or park[step_x][step_y] == 'X':
                flag = 1
                break
            
        if(flag == 0):
            x += nav[direction][0] * distance
            y += nav[direction][1] * distance
    
    answer = [x,y]
    return answer # 비슷하지만 작동

