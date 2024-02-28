num=input()
count=0
for i in num:
    if i=="4" or i=="7":
        count+=1

lucky=True
for i in str(count):
    if i=="4" or i=="7":
        continue
    else:
        lucky=False
if lucky:
    print("YES")
else:
    print("NO")
        