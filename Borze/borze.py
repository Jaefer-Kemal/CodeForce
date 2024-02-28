s=input().strip()
l=0
r=l+1
re=""
while l<len(s):
    
    if s[l]==".":
        re+="0"
        l+=1
        r=l+1
        
    elif s[l]=="-" and s[r]=="-":
        re+="2"
        l=r+1
        r=l+1
        
    elif  s[l]=="-" and s[r]==".":
        re+="1"
        l=r+1
        r=l+1
        
print(re)
