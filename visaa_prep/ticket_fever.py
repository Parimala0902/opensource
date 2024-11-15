t=int(input())
for _ in range(0,t):
    N,M=map(int,input().split())
    if N>M:
        print(N-M)
    else:
        print(0)
