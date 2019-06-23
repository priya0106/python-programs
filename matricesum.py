d=int(input())
arr=[list(map(int,input().split(" "))) for i in range(d)]
i,j=0,len(arr)-1
e,f=0,0
while i<len(arr):
	e+=arr[i][i]
	f+=arr[i][j]
	i+=1
	j-=1
print(e*f)
