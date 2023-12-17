def solution(name, yearning, photos):
    point = dict(zip(name, yearning))
    answer = []
    for photo in photos:
        answer.append(sum([point[name] for name in photo if name in point]))
    return answer
