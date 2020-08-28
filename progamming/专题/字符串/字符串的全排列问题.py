strs = "abcdefg"
result = []
def permute(strs):
    path = ""
    permutation(strs,path)
    return result
def permutation(strs,path):
    if not strs:
        result.append(path)
    for i in range(len(strs)):
        path += strs[i]
        permutation(strs[:i]+strs[i+1:],path)
        path = path[:-1]
print(len(permute(strs)))