string = "adeafgdc"
def solution(string):
    if not string:
        return 0
    max_length = 0
    queue = []
    str_list = list(string)
    for i in range(len(str_list)):
        if str_list[i] not in queue:
            queue.append(str_list[i])
        else:
            max_length = max(max_length,len(queue))
            queue.pop(0)
            queue.append(str_list[i])
    return max_length
print(solution(string))


