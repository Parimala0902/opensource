n=int(input())
a=list(map(int,input().split()))
ra=a[1:]+[a[0]]
print(*ra)
