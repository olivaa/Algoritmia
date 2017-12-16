def canoas(pesos,p):
	i=0
	j=len(pesos)-1
	cano=0
	while i<j:
		if pesos[i]+pesos[j]<=p:
			i+=1
		j-=1
		cano+=1
	if(i==j):
		cano+=1
	return cano

print(canoas([52,71,70,90],150))
