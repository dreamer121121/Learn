
def counting_inversion(A):
    if len(A) == 1:
        return A
    mid=len(A)//2
    left=A[:mid]
    right=A[mid:]
    ll=counting_inversion(left)
    rl=counting_inversion(right)
    return cross(ll,rl)


def cross(left,right):
    count=0
    while len(left)>0 and len(right)>







if __name__ == '__main__':
    A=[15,3,8,5,9,12,1,6,7]
    counting_inversion(A,len(A))