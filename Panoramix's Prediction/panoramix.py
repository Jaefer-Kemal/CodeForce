import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

x,y=map(int,input().split())

if 0<=x<=1 or 0<=y<=1:
    print("NO")

else:
    if not (is_prime(x) and is_prime(y)):
        print("NO")
    else:
        flag=True
        for i in range(x+1,y):
            if is_prime(i):
                print("NO")
                flag=False
                break
        if flag:
            print("YES")
            
        
    
