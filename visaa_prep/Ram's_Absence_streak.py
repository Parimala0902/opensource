n=int(input())
l=list(map(int,input().split()))
m=0
c=0
for n in l:
    if n==0:
        c=c+1
        m=max(m,c)
    else:
        c=0
print(m)
