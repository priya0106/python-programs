m=int(input())
y=list(map(int,input().split()))
c=0
for i in y:
    if(i<0):
        c=c+i 
print(c)
