b=int(input())
sum=0
if b<0:
    print("Invalid")
else:
    while(b>0):
        sum=sum+b
        b=b-1
    print(sum)
