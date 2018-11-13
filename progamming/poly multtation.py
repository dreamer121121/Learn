a = [1, 2, 3]
b = [3, 2, 2]
c = []

sum = 0
count=0
for k in range(len(a+b)-1):
    sum=0
    for i in range(len(a)):
        for j in range(len(b)):
            if i + j == k:
                sum += a[i] * b[j]
                count+=1
    c.append(sum)
# print(c)
print(count)