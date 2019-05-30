N,A,D=map(int,input().split())
sum=0
AP=A
for i in range(N):
  AP=A+D
  sum-sum+AP
print(sum)
