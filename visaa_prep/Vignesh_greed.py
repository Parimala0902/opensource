def perimeter(n,l):
    l.sort()
    for i in range(n-1,1,-1):
        if l[i-2]+l[i-1]>l[i]:
            return l[i-2]+l[i-1]+l[i]
    return -1
n=int(input())
l=list(map(int,input().split()))
print(perimeter(n,l))
