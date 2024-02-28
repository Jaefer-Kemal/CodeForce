x=[]
try:
    while True:
        x.append(list(map(int,input().split())))
except EOFError:
    pass
 
for i in range(len(x)):
    if 1 in x[i]:
        j=x[i].index(1)
        y=[i,j]
        break
i=y[0]
j=y[1]
count=abs(i-2)+abs(j-2)
 
print(count) 