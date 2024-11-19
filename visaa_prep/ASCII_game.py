s=input()
res=""
for char in s:
    if ord(char)>=65 and ord(char)<=90:
        res+=chr(ord(char)+32)
    if ord(char)>=97 and ord(char)<=122:
        res+=chr(ord(char)-32)
print(res)
