n,m=map(int,input().split())
a=list(map(int,input().split()))
n1=0
n2=0
for n in a:
    if n%m==0:
        n2=n2+n
    else:
        n1=n1+n
print(n2-n1)
