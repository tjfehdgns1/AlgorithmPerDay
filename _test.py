def solution(my_string):
    dic = dict.fromkeys(my_string)
    print(dic)
    answer = ''
    answer = answer.join(dic)
    print(answer)
    return ''.join(dict.fromkeys(my_string))

my_string = "We are the world"
result = solution(my_string)
print(result)