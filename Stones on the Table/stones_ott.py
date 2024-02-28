n=int(input())
s=input()
count=0
l=0
r=l+1
while r<n:
    if s[l]==s[r]:
        count+=1
    l=r
    r=l+1
print(count)
    
        