def FloydWarshall(G):
    A=[]    # A= (a_{ij}) n×n adjacency matrix of the digraph G
    
    for u in G:
        Au = []  # row of A correponding to vertex u 
        for v in G:
            if  v in G[u]:Au.append(G[u][v])
            elif u == v : Au.append(0)
            else: Au.append(float("inf"))     
        A.append(Au)
    
    Cnext = A
    
    for k in range(len(G)):
        C = Cnext
        for i in range(len(G)):
            for j in range(len(G)):
                if C[i][j] > C[i][k]+ C[k][j]:
                        Cnext[i][j] = C[i][k]+ C[k][j]
    return Cnext
            
G = {'s': {'u':10, 'x':5},
    'u': {'v':1, 'x':2},
    'v': {'y':4},
    'x':{'u':3,'v':9,'y':2},
    'y':{'s':7,'v':6}}

F = FloydWarshall(G)

V = "   "
for u in G:
    V = V + u + "   "
print(V)

i  = 0
for u in G:
    print(u,F[:][i])
    i = i + 1