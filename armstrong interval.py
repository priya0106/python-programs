a,b=list(map(int,input().split()))
for i in range(a,b):
  sum=0
  digit=0
  order=len(str(i))
  temp=i
  while(temp>0):
    digit=digit%10
    sum+=digit**order
    temp//=10
  if i==sum:
    print(sum)
