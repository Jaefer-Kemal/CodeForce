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
count=0
while i!=2 or j!=2:
    if i>2:
        i-=1
    elif i<2:
        i+=1
    elif j<2:
        j+=1
    elif j>2:
        j-=1
    count+=1
print(count)