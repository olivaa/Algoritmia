def maxim(X):
	m=[]
	for x in range(len(X)):
		m.append(1+max((m[j] for j in range (x) if X[j]<X[x]),default=0))
		
	return m

def vuelta_backpointer(X):
	m=[]
	b=[]
	maxim=0
	for x in range(len(X)):
		print(x)
		#print(len(m),x)
		m.append(1+max((m[j] for j in range (x) if X[j]<X[x]),default=0))
		for j in range(x):
			if X[j]<X[x] and m[j]+1==m[-1]:
				maxim=x
				print(m)
				print(j,m[j],m[-1])
				print(maxim)
				b.append(j)
				print(b)
	
	#print(b)
	a=[X[x] for x in b]
	#print(maxim)
	return a

X=[10,8,1,2,6,7,2]
print(maxim(X))
vuelta_backpointer(X)