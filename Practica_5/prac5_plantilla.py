import numpy as np
import heapq # a priority queue

def create_graph(N,maxvalue=1000):
  G = np.random.randint(maxvalue, size=(N, N))
  for i in range(N):
    G[i][i] = 0
    for j in range(i+1,N):
      m = min(G[i][j],G[j][i])
      G[i][j] -= m
      G[j][i] -= m
  return G

def generate_random_ordering(G):
  # let's assume that G is a square Numpy matrix of integers
  N = G.shape[0]
  return np.random.permutation(N)

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

def generate_greedy_ordering(G):
  # let's assume that G is a square Numpy matrix of integers
  N = G.shape[0]
  resul = []
  while len(resul)<N:
    noresul = list(set(range(N))-set(resul))
    aux = []
    for i in range(N):
      if i not in resul:
        score = (sum(G[j][i]-G[i][j] for j in resul) +
                 sum(G[i][j]-G[j][i] for j in noresul if j!=i))
        aux.append((score,i))
    print(resul,aux)
    score,choice = max(aux)
    resul.append(choice)
  return np.asarray(resul,dtype=np.int)

def evaluate_partial(G,ordering):
  # assume that G.shape is of type (N,N) and ordering.shape is of type
  # (N) and is a permutation of values 0,...,N-1
  N = len(ordering)
  return sum(G[ordering[i]][ordering[j]]-G[ordering[j]][ordering[i]]
             for i in range(N) for j in range(i+1,N))




def BranchAndBound(G):
  # ojo con graph <- "se mira pero no se toca"
  N = G.shape[0]

  def optimistic(s):
    # s es una lista de vertices entre 0 y N-1
    opt = 0
    desconocidos=[x for x in range (0,N) if x not in s]
    print("Desconocidos",desconocidos)
    # COMPLETAR:
    # sumamos la parte conocida:
    # en primer lugar, las aristas entre elementos conocidos:
    sum_conocidos=evaluate_partial(G,s)
    print(sum_conocidos)
    # luego la suma entre elementos conocidos y desconocidos:
    sum_con_des=0
    for x in s:
    	for i in desconocidos:
    		#print(evaluate_partial(G,[x,i]))
    		sum_con_des+=evaluate_partial(G,[x,i])
    # finalmente sumamos una estimación de la parte desconocida:
    suma_optimista=0
    for x in desconocidos:
    	for y in desconocidos:
    		print(suma_optimista)
    		suma_optimista+=G[x][y]

    opt=sum_conocidos+sum_con_des+suma_optimista

    return opt

  def branch(s):
    return (s+[i] for i in range(N) if i not in s)

  def is_complete(s):
    return len(s)==N

  A = [] # empty priority queue
  #alg. voraz
  x = generate_greedy_ordering(G)
  fx = optimistic(x) # equivale a evaluate quando is_complete(x)

  # anyadimos el estado inicial:
  s = []
  opt = optimistic(s)
  heapq.heappush(A,(-opt,s))
  iter = 0
  maxA = 0
  # bucle principal de ramificacion y poda:
  while len(A)>0 and -A[0][0] > fx: # PODA IMPLICITA
    iter += 1
    lenA = len(A)
    maxA = max(maxA,lenA)
    score_s, s = heapq.heappop(A)
    score_s = -score_s # ahora ya no está negado
    print("Iter. %04d |A|=%05d max|A|=%05d fx=%04d score_s=%04d" % \
          (iter,lenA,maxA,fx,score_s))
    for child in branch(s):
      if is_complete(child): # si es terminal
        # seguro que es factible
        # falta ver si mejora la mejor solucion en curso
        cota_child=optimistic(child)
        if cota_child > fx:
        	x,fx=child,cota_child
      else: # no es terminal
        # lo metemos en el cjt de estados activos si supera
        # la poda por cota optimista:
        opt_child=optimistic(child)
        if opt_child>fx:
        	heapq.heappush(A,(-opt_child,child))
  return x,fx
 
if __name__ == "__main__":
    N = 8
    #G = create_graph(N,5)
    G= np.array([[0, 8, 3, 2, 9],
	[3, 0, 3, 8, 2],
	[0, 2, 0, 6, 2],
	[4, 4, 8, 0, 0],
	[7, 7, 6, 2, 0]],dtype=np.int)
    print("G=",G)
    x,fx = BranchAndBound(G)
    greedy_ordering = generate_greedy_ordering(G)
    print("greedy ordering", greedy_ordering,evaluate(G,greedy_ordering))
    print("exacto",x,fx,evaluate(G,x))


