'''달리기 경주
문제 설명
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

제한사항
5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.
입출력 예
players	                                callings	                    result
["mumu", "soe", "poe", "kai", "mine"]	["kai", "kai", "mine", "mine"]	["mumu", "kai", "mine", "soe", "poe"]'''

def solution(players, callings):
    for call in callings :
        players[players.index(call) - 1], players[players.index(call)] = players[players.index(call)], players[players.index(call) - 1]
    return players # 리스트 안에 있는 값이 안바뀜
##############################################
def solution(players, callings):
    for call in callings:
        index = players.index(call)
        if index != 0:
            players[index - 1], players[index] = players[index], players[index - 1]
    return players # 테스트케이스 시간 초과 
###########################################
def solution(players, callings):
    player_dict = {player: index for index, player in enumerate(players)}
    for call in callings:
        index = player_dict[call]
        if index != 0:
            players[index-1], players[index] = players[index], players[index-1]
            player_dict[players[index]] = index
            player_dict[players[index-1]] = index - 1
    return players # 리스트의 인덱스를 하나하나 찾는거 보단 딕셔너리를 쓰는게 효율적
