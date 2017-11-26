
def cadena(lista):
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
	volver=0;
	maximo=max(aux);
	for x in range(len(lista)-1,0,-1):
		if(aux[x]==maximo):
			volver=x;
			break;

	m=maximo;
	aux=[0]*m;
	while(m!=0):
		aux[m-1]=lista[volver]
		volver=backpointer[volver]
		m=m-1;

	return aux


l=[210, 816, 357, 107, 889, 635, 733, 930, 842, 542];
l2=[1, 15, 20, 12,30,26,40,50, 45];

aux=cadena(l2);








