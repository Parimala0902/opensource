s=input()
r=[]
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        r.append(f"{s[i-1]}{count}")
        count = 1
r.append(f"{s[-1]}{count}")
print("".join(r))
