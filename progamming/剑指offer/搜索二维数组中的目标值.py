#思路一：抓住每一行的最小的数即最左边的数
def Find(target,array):
    row_cnt = len(array)
    col_cnt = len(array[0])
    i = row_cnt-1
    j = 0
    while i >=0 and j < col_cnt:
        if array[i][j] == target:
            return True
        if array[i][j] > target:
            i -=1
        elif array[i][j] < target:
            j += 1
    return False

#思路二：将每一行看成递增数组二分查找
def Find2(target,array):
    row_cnt = len(array)
    col_cnt = len(array[0])
    def find_in_row(row,start,end):
        print(start,end)
        mid = (start+end)//2
        mid_num = row[mid]
        if target == mid_num:
            return True
        if start == end and mid_num != target:
            return False
        if target > mid_num:
            return find_in_row(row,mid+1,end) #递归实现二分法
        elif target < mid_num:
            return find_in_row(row,mid-1,end)

    for i in range(row_cnt):
        row = array[i]
        print('i',i)
        if find_in_row(row,0,col_cnt-1):
            return True

    return False

print(Find2(12,[[1,2,3],[4,5,6],[7,8,9]]))