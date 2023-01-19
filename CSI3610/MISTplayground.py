def newgraph(v=None): # By default empty. Can contain a si
    return {v:{}} if v is not None else {}
def nodes(G): # A list of all nodes
    return list(G)
def nodecount(G): # The number of nodes
    return len(G)
def addarc(G,e):
    (u,v,w) = e
    H=G.get(u,None)
    if H is None:
        G[u]={v:w}
    else:
        G[u][v]=w
    H=G.get(v,None)
    if H is None:
        G[v]={}
def addedge(G,e): # Adds (u,v) and (v,u)
    (u,v,w) = e
    addarc(G,(u,v,w))
    addarc(G,(v,u,w))
def neighbors(G,u): # Returns a list of neighbors
    a=[]
    for v,w in G[u].items():
        a.append((v,w))
    return a
def arcs(G): # A list of triples (u,v,w)
    all=[]
    for u in G.keys():
        for v,w in neighbors(G,u):
            all.append((u,v,w))
    return all
def edges(G): # A list of triples (u,v,w)
    all=[]
    for u in G.keys():
        for v,w in neighbors(G,u):
            if u<v:
                all.append((u,v,w))
    return all
def nodeingraph_p(v,G): # True iff node is in the graph
    H = G.get(v,False)
    return H != False
def boundaryedge_p(u,v,G): # True iff u is in G and v is not
    H=nodeingraph_p(u,G)
    return H!=False and not nodeingraph_p(v,G)
def weight(edge):
    return edge[2]
def newheap(n):
    return [0]*(n+1)
def insert(a,e):
    a[0] = a[0] + 1
    a[a[0]] = e
    heapfixup(a,a[0])
def heapfixup(a,i):
    while i > 1:
        p = i // 2
        if weight(a[p]) > weight(a[i]): # We compare the edge wei
            a[p],a[i] = a[i],a[p]
            i = p
        else:
            return
def extractsmallest(a):
    e,a[1],a[0] = a[1],a[a[0]],a[0]-1
    heapfixdown(a,1)
    return e
def heapfixdown(a,i):
    while 2*i <= a[0]:
        c = 2*i
        if c+1 <= a[0]:
            if weight(a[c+1]) < weight(a[c]):
                c = c+1
        if weight(a[i]) > weight(a[c]):
            a[i],a[c] = a[c],a[i]
            i = c
        else:
            return
def prim(G):
    V = nodes(G)
    n = len(V)
    q = newheap(n*n)
    T = newgraph(0)
    for (v,w) in neighbors(G,0):
        insert(q,(0, v, w))
    while nodecount(T) < n:
        (u,v,w) = extractsmallest(q)
        if boundaryedge_p(u,v,T):
            addedge(T,(u,v,w))
            for (t,w) in neighbors(G,v):
                if not nodeingraph_p(t,T):
                    insert(q,(v,t,w))
    return T

G = newgraph()
for e in [(0,1,1),(0,3,2),(1,2,2),(1,4,5),(2,3,1),(3,4,1)]:
#for e in [(0, 9, 9),(9, 11, 11), (9, 41, 41), (11, 32, 32), (11, 31, 31), (41, 12, 12), (12, 13, 13), (12, 42, 42)]:
    addedge(G,e)
print(G)
print(nodes(G))
T=prim(G)
print(T)
total=0
for (u,v,w) in edges(T):
    total += w
print('Total MST cost is ',total)

print("\n")

B = newgraph()
for e in [(9, 11, 11), (9, 41, 41), (11, 32, 32), (11, 31, 31), (41, 12, 12), (12, 13, 13), (12, 42, 42)]:
    addedge(B, e)
print(nodes(B))
print(neighbors(B, neighbors(B, 41)[1][0])[1][0])
print(neighbors(B, neighbors(B, 41)[1][0])[2][0])
print(neighbors(B, 41)[1][0])
#print(neighbors(B, 12)[2][0])
n = []
n += [neighbors(B, neighbors(B, neighbors(B, 9)[1][0])[1][0])[1][0]]
print(n)

print("\n")

def independentify(G, root, n = []):
    x = []
    for neighbor in neighbors(G, root):
        if(len(neighbor) >= 2):
            n += [neighbor[0]]
    for i in n:
        x = []
        print(i)
        for neighbor in neighbors(G, i):
            x += [neighbor[0]]
        print(x)
        x.pop(0)
        n += x
    #return neighbors(G, root)
    return n

print(independentify(B, 9))

print("\n")

#B = newgraph()
#addedge(B, (0,1,1))
#print(B)



# FOR v, SET UP AN m_size VARIABLE THAT RETURNS
# THE MAX INDEPENDENT SIZE ROOTED AT v
#def MIST(v):
    # SET THIS EQUAL TO THE SUM OF MIST(u)
    # WHERE u IS A NEIGHBOR OF v
    #skip = 0

    #keep = 1
    # for all "second/grandchild" neighbors s of v:
        # add s.m_size to keep
    # v.m_size = max(skip, keep)
    #return v.m_size
