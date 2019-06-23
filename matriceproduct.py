h=int(input())
arr=[list(map(int,input().split(" "))) for i in range(h)]
i,j=0,len(arr)-1
e,f=1,1
while i<len(arr):
	e*=arr[i][i]
	f*=arr[i][j]
	i+=1
	j-=1
print(e+f)
