def FirstNotRepeatingChar(s):
    if len(s) == 0:
        return -1
    result_array = {}
    for i in range(len(s)):
        if s[i] not in result_array.keys():
            result_array[s[i]] = 1
        else:
            result_array[s[i]] += 1
    for key, value in result_array.items():
        if result_array[key] > 1:
            continue
        elif result_array[key] == 1:
            return list(s).index(key)
    return -1
print(FirstNotRepeatingChar('abaccdeff'))