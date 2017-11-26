# -*- coding: utf-8 -*-
"""
Autors: Alejandro Oliva Rodríguez
        Joan Masanet López
"""
import sys
import random

literal=[]
def read_cnf_dimacs(filename):
  linenumber = 0
  num_variables = 0
  num_clauses = 0
  clauses = []
  try:
    with open(filename) as f:
      for line in f:
        linenumber += 1
        line = line.split()
        if len(line)==0 or line[0]=='c': continue
        if len(line)==4 and line[0]=='p' and line[1]=='cnf':
          num_variables = int(line[2])
          num_clauses = int(line[3])
          break;
        sys.exit("error reading cnf file '%s' at line %d" % (filename,linenumber))
      for line in f:
        linenumber += 1
        line = line.split()
        if len(line)==0 or line[0]=='c': continue
        clause = [int(x) for x in line]
        if clause[-1] != 0:
          sys.exit("error reading cnf file '%s' at line %d expecting 0 at last position" \
                   % (filename,linenumber))
        del clause[-1] # remove last element
        if any(abs(x)>num_variables for x in clause):
          sys.exit("error reading cnf file '%s' at line %d variable out of range" \
                   % (filename,linenumber))
        clauses.append(clause)
  except ValueError:
      sys.exit("error reading cnf file '%s' at line %d parsing int" % (filename,linenumber))
  if len(clauses) != num_clauses:
      sys.exit("error reading cnf file '%s' number of clauses differ" % (filename,))
  # just in case, remove empty clauses
  clauses = [clause for clause in clauses if len(clauses)>0]
  return num_variables,clauses

def choose_literal(clauses):
  smallest = min(len(clause) for clause in clauses)
  variables = set(y for clause in clauses for y in clause if len(clause)==smallest)
  #return random.choice(tuple(variables))
  return variables.pop()

def simplify(clauses,literal):
    s=[[i for i in c if i!=-literal] for c in clauses if literal not in c]

    if len(s)==0:return True
    elif [] in s: return False
    else: return s


def check(formula,listofliterals):
  # determines if the list of literals is able to assign a True value
  # to the formula
  print(formula,listofliterals)
  for literal in listofliterals:
    formula = simplify(formula,literal)
    print("Despejando literal",literal)
    print(formula)
    if isinstance(formula,bool):
      return formula
  # at this point, the formula has not been fully simplified
  return False

def backtracking(formula):
  if len(formula)==0: return True
  lit=choose_literal(formula)
  for c in (lit,-lit):
    f=simplify(formula,c)
    if f is not False:
      if f is True:
        literal.append(c)
        return literal
      resul=backtracking(f)
      if resul:
        literal.append(c)
        return resul
  return None

def unit_propagation(clauses):
  
  asignados=[]
  clau_uni=[i for i in clauses if len(i)==1]

  while len(clau_uni)!=0:
    clau_n_uni=[i for i in clauses if len(i)>1]
    
    for x in clau_uni:
      asignados.append(x[0])
      clau_uni=[i for i in clau_uni if x[0] not in i]
      clau_n_uni=[[i for i in c if i!=-x[0]] for c in clau_n_uni if x[0] not in c]
    
    
    clauses=clau_uni+clau_n_uni
    clau_uni=[i for i in clauses if len(i)==1]


  if len(clauses)==0:return True,asignados
  elif [] in clauses: return False,asignados
 
  return clauses,asignados

def pure_literal_elimination(clauses):
  #print("Clausulas",clauses)
  positivos=set()
  for i in clauses:
    for j in i:
      if j>=0:positivos.add(j)

  negativos=set()
  for i in clauses:
    for j in i:
      if j<0:negativos.add(j*-1)  

  puros=[]
  for i in positivos:
    if i not in negativos: puros.append(i)

  for i in negativos:
    if i not in positivos: puros.append(i*-1)

  claus_aux=[i for i in clauses]
  for x in puros:
    for i in clauses:
      if x in i:
        if i in claus_aux:
          claus_aux.remove(i)

  if len(claus_aux)==0:return True,puros
  return claus_aux,puros

def dpll(formula):
  if len(formula)==0: return True

  u=unit_propagation(formula)

  for i in u[1]:
    literal.append(i)
  if u[0] is True:
    return literal
  elif u[0] is False:
    return False
  formula=u[0]

  pur=pure_literal_elimination(formula)
  for i in pur[1]:
    literal.append(i)
  if pur[0] is True:
    return literal

  formula=pur[0]

  if formula!=False:
    resul=backtracking(formula)

  return resul

######################################################################
######################       MAIN PROGRAM       ######################
######################################################################
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print('\n%s dimacs_cnf_file\n' % (sys.argv[0],))
    sys.exit()
        
  file_name = sys.argv[1]
  num_variables,clauses = read_cnf_dimacs(file_name)
  # replace backtracking by dpll when checking dpll
  #resul = dpll(clauses)
  #Prueba 
 
  resul = backtracking(clauses)
  #print(resul,"SOL")
  if resul != None:
    print("We have found a solution:",resul)
    print("The check returns:",check(clauses,resul))
  else:
    print("Not solution has been found")

