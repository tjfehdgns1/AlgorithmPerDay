def solution(players, callings):
    player_dict = {player: index for index, player in enumerate(players)}
    for call in callings:
        index = player_dict[call]
        if index != 0:
            players[index-1], players[index] = players[index], players[index-1]
            player_dict[players[index]] = index
            player_dict[players[index-1]] = index - 1
    return players

