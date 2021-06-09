t = int(input())
for i in range(t):
	n,m,k = map(int,input().split())
	l = list(map(int,input().split()))
	x = {}
	for j in range(n):
		x[j] = []
	for j in range(n):
		temp = l[j]
		x[temp-1].append(j+1)
	print(x)
	j=0
	me = l[0]
	while m>0 and j+1<=me:
		m-=len(x[j])
		print(m)
		k-=1
		j+=1
	if j-1>me:
		print("YES")
	elif j==me and m<0:
		print("MAYBE")
	else:
		print("NO")