s=input()
up=0
lo=0
for i in s:
    if i.isupper():
        up+=1
    else:
        lo+=1
if up>lo:
    print(s.upper())
else:
    print(s.lower())