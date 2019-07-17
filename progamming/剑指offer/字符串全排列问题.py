
def Permutation(ss):
    if len(ss) <=0:
        return []
    res = list()
    perm(ss,res,'')
    print("---递归结束后的res---",res)
    #以上是求n个不同元素的全排列,若字符串中有重复的字母，则最终的全排列的数量一定小于n个不同字母的全排列的数量。
    uniq = list(set(res)) #利用set去重
    uniq.sort()
    return uniq

def perm(ss,res,path):
    if ss=='':
        res.append(path) #递归的终止条件，当前path已经遍历了字符串中的所有字母
    else:
        for i in range(len(ss)):
            perm(ss[:i]+ss[i+1:],res,path+ss[i])

print(Permutation('a'))
