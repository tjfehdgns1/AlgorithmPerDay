'''실패율

슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

제한사항
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
입출력 예
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]'''

def solution(N, stages):
    values = range(1,N+1)
    keys = []
    for i in values :
        keys.append(stages.count(i))

    d = dict(zip(values, keys))
    keys.sort(reverse = True)
    return [d[k] for k in keys] # 오류

def solution(N, stages):
    c = []
    f = []
    left = len(stages)
    
    for i in range(1,N+1) :
        c.append(stages.count(i))
        f.append((i,c[i-1]/left))
        left -= stages.count(i)

    f.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, f in f] # 런타임 에러, 최대 3499.57ms

from collections import Counter

def solution(N, stages):
    # Counter 클래스를 사용하여 각 스테이지까지 도전한 사용자 수와 실패한 사용자 수를 계산
    counter = Counter(stages)
    # 실패율을 저장할 리스트 생성
    failure_rates = []
    # 스테이지 번호를 1부터 N까지 반복하면서 실패율 계산
    for i in range(1, N+1):
        # 해당 스테이지까지 도전한 사용자 수 계산
        num_users = sum([count for stage, count in counter.items() if stage >= i])
        # 해당 스테이지에서 실패한 사용자 수 계산
        num_failures = counter[i] if i in counter else 0
        # 실패율 계산하여 리스트에 추가
        failure_rates.append((i, num_failures/num_users if num_users != 0 else 0))
    # 실패율을 내림차순으로 정렬
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    # 정렬된 실패율에서 스테이지 번호만 추출하여 리스트로 반환
    return [stage for stage, failure_rate in failure_rates] # 최대 45ms

def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer # 24.95ms
