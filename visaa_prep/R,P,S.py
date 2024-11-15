v,c = map(str,input().split())
if (v=='R' and c=='S') or (v=='S' and c=='P') or (v=='P' and c=='R' ):
    print("Vignesh")
elif (c=='R' and v=='s') or (c=='S' and v=='P') or(c=='P' and v=='R'):
    print("Charan")
else:
    print("NULL")
