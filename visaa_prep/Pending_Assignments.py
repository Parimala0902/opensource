x,y,z=map(int,input().split())
tc=x*y
tt=z*24*60
if tc <= tt:
    print("YES")
else:
    print("NO")
