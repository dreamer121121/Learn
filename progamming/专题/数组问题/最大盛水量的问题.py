def maxArea(l):
    i = 0
    j = len(l)-1
    maxarea = 0
    while i < j:
        under = j-1
        minpillar = min(l[i],l[j])
        area = minpillar*under
        if area > maxarea:
            maxarea = area
        if l[i] <= l[j]:
            i += 1
        else:
            j -=1
    return maxarea
print(maxArea([1,8,6,2,5,4,8,3,7]))
