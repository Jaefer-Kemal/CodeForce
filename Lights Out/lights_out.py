press=list()
# We assume that the grid is 3 x 3
for _ in range(3):
    press.append(list(map(int,input().split())))
# Originally all the lights are ON [ON=1, OFF=0]
temp=[[1,1,1],[1,1,1],[1,1,1]]

for i in range(3):
    for j in range(3):
        # if the number of time he pressed is even it will remain the samw
        if press[i][j]%2!=0: 
            #Three Possibilities
            if (j==0 or j==2) and (i==0 or i==2):  
            # When they are pressing at the corner of the grid         
                    temp[i][j]= 1 if temp[i][j]==0 else 0
                    temp[1][j]= 1 if temp[1][j]==0 else 0
                    temp[i][1]= 1 if temp[i][1]==0 else 0
                    
            elif i==1 and j==1:
            #Pressing at the middle
                temp[i][j]= 1 if temp[i][j]==0 else 0
                temp[0][j]= 1 if temp[0][j]==0 else 0
                temp[i][0]= 1 if temp[i][0]==0 else 0
                temp[i][2]= 1 if temp[i][2]==0 else 0
                temp[2][j]= 1 if temp[2][j]==0 else 0
                
            else:
            # Pressing inbetween except middle when [i=j+1 or j=i+1]
                temp[i][j]= 1 if temp[i][j]==0 else 0
                temp[1][1]= 1 if temp[1][1]==0 else 0
                if j==0 or i==0:
                    temp[0][0]= 1 if temp[0][0]==0 else 0
                    if i==1:
                        temp[2][0]= 1 if temp[2][0]==0 else 0
                    else:
                        temp[0][2]= 1 if temp[0][2]==0 else 0
                elif j==2 or i==2:
                    temp[2][2]= 1 if temp[2][2]==0 else 0
                    if i==1:
                        temp[0][2]= 1 if temp[0][2]==0 else 0
                    else:
                        temp[2][0]= 1 if temp[2][0]==0 else 0        
                    
for row in temp:
    for l in row:
        print(str(l),end="")
    print()