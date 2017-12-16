
#calculamos la duracion de un concierto
def duracion(s_t):
	s,t = s_t
	return t-s

def dos_voraces(lista):
	#per cada concert el tregem ordenats per duracio
	#que es lo que vol el soci
	for concierto in sorted(lista,key=duracion):
		print(concierto)



dos_voraces([(1,3),(2,5),(4,7),(4,6)])