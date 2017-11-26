


def ejercicio4(lista):
	
	for i in range(0,len(lista)):
		for j in range(0,i):
			if( lista[i]> lista[j] and aux[i]<=aux[j]):
				aux[i]=aux[j]+1
				aux2[i]=j;

	return aux





"""
aux=[1,1,1,1,1,1,1,1,1,1];

l=[210, 816, 357, 107, 889, 635, 733, 930, 842, 542];
aux2=[0]*len(l);
cadena(l);
maximo=max(aux);

print("Valor de los elementos-> ",aux)
print(aux2);

volver=0;
for x in range(len(l)-1,0,-1):
	if(aux[x]==maximo):
		volver=x;
		break;

for i in range(0,maximo):
	print(aux[])

"""

print("La subsecuencia mas larga es->",maximo)

