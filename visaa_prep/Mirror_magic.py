n=int(input())
m=[input().split() for _ in range(n)]
for r in m:
    print(" ".join(r[::-1]))
