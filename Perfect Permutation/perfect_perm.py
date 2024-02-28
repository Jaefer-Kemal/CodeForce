#from itertools import permutations

n = int(input())
if n%2!=0:
    print(-1)
else:
    p=[str(i) for i in range(1, n + 1)]
    l=0
    r=l+1
    while r<n:
        temp=p[l]
        p[l]=p[r]
        p[r]=temp
        l=r+1
        r=l+1
    print(" ".join(p))



##Time complexity is O(n!)
'''
else:    
    perm = [j for j in permutations([str(i) for i in range(1, n + 1)])]
    flag = True

    for row in perm:
        for j in range(1, len(row) + 1):
            if row[j - 1] == str(j):
                flag = False
                break
        if flag:
            print(" ".join(row))
            break
        else:
            flag = True
'''
