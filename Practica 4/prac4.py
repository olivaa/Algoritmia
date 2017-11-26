import numpy as np

def create_graph(N,maxvalue=1000):
  G = np.random.randint(maxvalue, size=(N, N))
  for i in range(N):
    G[i][i] = 0
  return G

def process_graph(G):
  	N = G.shape[0]
  	for i in range(0,N):
  		for j in range(0,N):
  			G[i][j]=G[i][j]-G[j][i]
  			G[j][i]=0
  	print(G)
  	return G

def generate_random_ordering(G):
  # let's assume that G is a square Numpy matrix of integers
  N = G.shape[0]
  return np.random.permutation(N)

def generate_greedy_ordering(G):
  # let's assume that G is a square Numpy matrix of integers 
  N = G.shape[0] 
  aux=G.shape[0] 
  candidatos= [x for x in range(0,N)] 
  fijados=[] 
 
  #fins que no estigen fixats tots els vertex 
  while aux>0: 
    val_max=[] 
    for i in candidatos: 
      score=sum(G[j][i]-G[i][j] for j in fijados) 
      val_max.append((score+sum(G[i][j]-G[j][i] for j in range(0,N) if j not in fijados),i)) 
 
    print("Fijados",fijados,"elijo el máximo de",val_max) 
    fijados.append(max(val_max)[1]) 
    candidatos= [x for x in range(0,N) if x not in fijados] 
    aux-=1 
 
  return fijados 

def alternativa(G):
  # let's assume that G is a square Numpy matrix of integers
  N = G.shape[0]
  aux=G.shape[0]
  #candidats 
  candidatos= [x for x in range(0,N)]
  fijados=[]

  #fins que no estigen fixats tots els vertex
  while aux>0:
  	val_max=[]
  	#creem una matriu on anirem actualizantla introduint els valor corresponents al vertex fixat
  	g_scores=create_graph(N,1)
  	for i in candidatos:
  		#cree matriu nova
  		g_aux=create_graph(N,1)
  		#li afegim els valor dels vertex ja fixats
  		g_aux=g_aux+g_scores

  		for j in range(0,N):
  			g_aux[i][j]=G[i][j]
  			g_aux[j][i]=G[j][i]

  		#a la funcio evaluate li pasem un vector amb els vertex ja fixats + el que estem explorant i per ultim la resta de vertes
  		#aquest ultims vertex no afecten al resultat ja que el seu valors es 0
  		q=fijados+[i]+[x for x in range(N) if x not in fijados and x != i]
  		val=evaluate(g_aux,q)
  		#afegim el resultat per a despres elegir el millor vertex
  		val_max.append((val,i))

  	print("Fijados",fijados,"elijo el máximo de",val_max)
  	#agafem el vertex en mes puntuacio
  	maxim=max(val_max)
  	#l'afegim a fijados
  	fijados.append(maxim[1])
  	#actualizem score
  	for j in range(0,N):
  			#print(i,j)
  			g_scores[maxim[1]][j]=G[maxim[1]][j]
  			g_scores[j][maxim[1]]=G[j][maxim[1]]

    #actualizamos candidatos
  	candidatos=[x for x in candidatos if x != maxim[1]]
  	#rint(fijados,"maxim",g_scores)
  	aux-=1

  return fijados
  
def evaluate(G,ordering):
  # assume that G.shape is of type (N,N) and ordering.shape is of type
  # (N) and is a permutation of values 0,...,N-1
  N = G.shape[0]
  return sum(G[ordering[i]][ordering[j]]-G[ordering[j]][ordering[i]]
             for i in range(N) for j in range(i+1,N))

def show_evaluate(G,ordering):
  N = G.shape[0]
  positivos = list(G[ordering[i]][ordering[j]] for i in range(N) for j in range(i+1,N))
  negativos = list(G[ordering[j]][ordering[i]] for i in range(N) for j in range(i+1,N))
  vpos = sum(positivos)
  vneg = sum(negativos)
  resul = vpos-vneg
  print("(" + ",".join(map(str,positivos))+") - (" + ",".join(map(str,negativos))+
        ") = ",vpos, "-", vneg, "=", resul)
  return resul

  
# si pruebas con este grafo:
G= np.asarray([[0, 8, 3, 2, 9],
               [3, 0, 3, 8, 2],
               [0, 2, 0, 6, 2],
               [4, 4, 8, 0, 0],
               [7, 7, 6, 2, 0]],dtype=np.int)
# el algoritmo voraz hace estos pasos:
# [] [(8, 0), (-5, 1), (-10, 2), (-2, 3), (9, 4)]
# [4] [(4, 0), (5, 1), (-2, 2), (2, 3)]
# [4, 1] [(-6, 0), (0, 2), (10, 3)]
# [4, 1, 3] [(-2, 0), (4, 2)]
# [4, 1, 3, 2] [(-8, 0)]
# y termina dando como resultado:
# [4, 1, 3, 2, 0]
# con valor 10

# este trozo prueba ejemplos aleatorios:
#N = 30
#G = create_graph(N,100)
#print("G=",G)
#random_ordering = generate_random_ordering(G)

#G=process_graph(G)
greedy_ordering = generate_greedy_ordering(G)
#print("random",evaluate(G,random_ordering))
print("greedy",evaluate(G,greedy_ordering))

