a=int(input())
fac=1
if a==0:
    print("1")
elif a>1:
    for i in range(1,a+1):
        fac=fac*i 
    print(fac)
