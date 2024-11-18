N=int(input())
num=1
for i in range(1,N+1):
    r=[str(num+j) for j in range(i)]
    print(" ".join(r))
    num = num+i
