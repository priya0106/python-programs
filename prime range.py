a,b=list(map(int,input().split()))
if(a>0 and b>0):
  for i in range(a+1,b):
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      print(i)
 
