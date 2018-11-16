import random
A=[1,0,2,0,1,1,2,2,1]
temp=[]
t=len(A)
def color(A):
    z=-1
    t=len(A)
    i=0
    while i < t:

        if A[i] == 0:
            z+=1
            A[z],A[i]=A[i],A[z]

        if A[i] == 1:
            pass

        while A[i] == 2:
            t-=1
            A[t],A[i] = A[i],A[t]
        i+=1

color(A)
print(A)