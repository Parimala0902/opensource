def ra(a,k,n):
    k=k%n
    return a[-k:]+a[:-k]
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(*ra(a,k,n))
