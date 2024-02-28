n1=input()
n2=input()
r=0
while r<len(n1):
    res=int(n1[r])+int(n2[r])
    if res==0 or res>1:
        print("0",end="")
    else:
        print("1",end="")
    r+=1