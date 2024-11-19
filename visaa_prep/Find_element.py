n=int(input())
arr=list(map(int,input().split()))
x=int(input())
l,r=0,len(arr)-1
found=False
while l <= r:
    m=(l+r)//2
    if arr[m]==x:
        print(m)
        found=True
        break
    elif arr[m]<=x:
        l=m+1
    else:
        r=m-1
if not found:
        print(-1)
