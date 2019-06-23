a=str(input())
for i in range(len(a)):
    if(a[i].islower()==True):
        print(a[i].upper(),end="")
    else:
        print(a[i].lower(),end="")
