num=int(input())
if num<=100000:
  order=len(str(num))
sum=o
temp=num
while temp>0:
  digit=temp%10
  sum+=digit**order
  temp//=10
if num==sum:
  print("yes")
else:
  print("no")
