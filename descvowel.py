n=int(input())
v=['a','e','i','o','u','A','E','I','O','U']
cnt=0
a=[]
for i in range(n):
    s=input()
    for i in s:
        if i in v:
            cnt+=1 
    a.append([s,cnt])
    cnt=0
a.sort(key=lambda x:x[1],reverse=True)
for i in range(n):
    print(a[i][0])
