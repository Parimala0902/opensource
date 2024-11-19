def count_vowels_consonants(s):
    vowels=set('aeiouAEIOU')
    vc=cc=0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vc=vc+1
            else:
                cc=cc+1
    return vc,cc
s=input()
v,c=count_vowels_consonants(s)
print(f"{v},{c}")
