n, t=map(int,input().split())
q=list(input().strip())

while t>0:
    l=0
    r=l+1
    t
    while r < n:
        if q[l]=="B" and q[r]=="G":
            q[l]="G"
            q[r]="B"
            l=r+1
            r=l+1
        else:
            l+=1
            r=l+1
    t-=1
    
print( "".join(q))
    
        
    