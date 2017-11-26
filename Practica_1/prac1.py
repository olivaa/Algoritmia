
def ejercicio2(lista):

	aux=[1]*len(lista);
	for i in range(0,len(lista)):
		for j in range(0,i):
			if( lista[i]> lista[j] and aux[i]<=aux[j]):
				aux[i]=aux[j]+1
	return aux


def ejercicio3(lista):
	return max(ejercicio2(lista))
	

def ejercicio4(lista):
	backpointer=[0]*len(lista);
	aux=[1]*len(lista);
	aux2=[0]*len(lista);
	#Donem el valor de la subsecuencia mes llarga per a cada element 
	#de forma iterativa com s'ha fet en els exercicis anteriors
	for i in range(0,len(lista)):
		for j in range(0,i):
			if( lista[i]> lista[j] and aux[i]<=aux[j]):
				aux[i]=aux[j]+1
				aux2[i]=j;
				backpointer[i]=j;
	#Buscar la posicio de la solucio másxima comensant per d'arrere 
	#S'ha fet ús de backpointers
	v=0;
	maximo=max(aux);
	for x in range(len(lista)-1,0,-1):
		if(aux[x]==maximo):
			v=x;
			break;
	#En la seguent llista s'aniran incluint els elements que conformen la subsecuencia 
	#més llarga		
	sol=[];
	while(maximo!=0):
		sol=[lista[v]]+sol
		v=backpointer[v]
		maximo=maximo-1;

	return sol




"""
#exercici2
p2=ejercicio2([210, 816, 357, 107, 889, 635, 733, 930, 842, 542]);
#exercici1
p3=max(p2);

print(p2)
print(p3)
"""
