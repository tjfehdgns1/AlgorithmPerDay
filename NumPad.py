'''키패드 누르기
문제 설명
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며,
 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

[제한사항]
numbers 배열의 크기는 1 이상 1,000 이하입니다.
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
hand는 "left" 또는 "right" 입니다.
"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.
입출력 예
numbers	                            hand        result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	    "right"	"LLRLLRLLRL"'''

def solution(numbers, hand):
    answer = ''
    rule = {
        'L' : [1,4,7],
        'R' : [3,6,9],
        'm' : [2,5,8,0]
    }
    
    l_hand, r_hand = '*', '#'
    
    for num in numbers :
        if num in rule['L'] :
            answer += 'L'
            l_hand = num
        elif num in rule['R'] :
            answer += 'R'
            r_hand = num
        else :
            l_distance = abs(rule['m'].index(num) - rule['m'].index(l_hand))
            r_distance = abs(rule['m'].index(num) - rule['m'].index(r_hand))
            
            if l_distance < r_distance:
                answer += 'L'
                l_hand = num
            elif l_distance > r_distance:
                answer += 'R'
                r_hand = num
            else: 
                if hand == 'left':
                    answer += 'L'
                    l_hand = num
                else: 
                    answer += 'R'
                    r_hand = num 
    return answer
# wrong


def solution(numbers, hand):
    answer = ''
    left, right = (0, 3), (2, 3)  # 왼손 시작 위치, 오른손 시작 위치
    keypad = [(i, j) for i in range(3) for j in range(3)] + [(3, 1)]
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = keypad[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            right = keypad[num]
        else:
            num_pos = keypad[num]
            l_distance = abs(left[0] - num_pos[0]) + abs(left[1] - num_pos[1])
            r_distance = abs(right[0] - num_pos[0]) + abs(right[1] - num_pos[1])
            
            if l_distance < r_distance:
                answer += 'L'
                left = num_pos
            elif l_distance > r_distance:
                answer += 'R'
                right = num_pos
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num_pos
                else:
                    answer += 'R'
                    right = num_pos
                    
    return answer # wrong




def solution(numbers, hand):
    # 시작 위치
    left_pos, right_pos = '*', '#'
    
    # 거리 계산 함수
    def get_distance(pos1, pos2):
        pos = {'1':(0,0), '2':(0,1), '3':(0,2),
               '4':(1,0), '5':(1,1), '6':(1,2),
               '7':(2,0), '8':(2,1), '9':(2,2),
               '*':(3,0), '0':(3,1), '#':(3,2)}
        pos1_x, pos1_y = pos[pos1]
        pos2_x, pos2_y = pos[pos2]
        return abs(pos1_x - pos2_x) + abs(pos1_y - pos2_y)
    
    # 번호별로 손 선택
    answer = ''
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = str(num)
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = str(num)
        else:
            # 거리 계산
            left_dist = get_distance(left_pos, str(num))
            right_dist = get_distance(right_pos, str(num))
            # 가까운 손 선택
            if left_dist < right_dist:
                answer += 'L'
                left_pos = str(num)
            elif left_dist > right_dist:
                answer += 'R'
                right_pos = str(num)
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = str(num)
                else:
                    answer += 'R'
                    right_pos = str(num)
                    
    return answer # 거리 계산을 딕셔너리와 튜플로
