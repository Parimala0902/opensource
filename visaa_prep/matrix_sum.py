n=int(input())
m=[]
for _ in range(n):
    r=list(map(int,input().split()))
    m.append(r)
row_sum=[0]*n
for i in range(n):
    row_sum[i] = sum(m[i])
col_sum=[0]*n
for j in range(n):
        col_sum[j]=sum(m[i][j] for i in range(n))
A=[]
for i in range(n):
    A.append(row_sum[i]+col_sum[i])
print(*A)
