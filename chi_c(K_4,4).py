#a correspondence covergraph of K_{4,4} with lists of length 3 and chi_c=4

Z=[(0, 1), (0, 2), (0, 12), (0, 15), (0, 18), (0, 21), (1, 2), (1, 13), (1, 16), (1, 19), (1, 22), (2, 14), (2, 17), (2, 20), (2, 23), (3, 4), (3, 5), (3, 12), (3, 17), (3, 19), (3, 23), (4, 5), (4, 13), (4, 15), (4, 20), (4, 22), (5, 14), (5, 16), (5, 18), (5, 21), (6, 7), (6, 8), (6, 12), (6, 15), (6, 18), (6, 22), (7, 8), (7, 13), (7, 16), (7, 19), (7, 23), (8, 14), (8, 17), (8, 20), (8, 21), (9, 10), (9, 11), (9, 12), (9, 15), (9, 18), (9, 23), (10, 11), (10, 13), (10, 16), (10, 19), (10, 21), (11, 14), (11, 17), (11, 20), (11, 22), (12, 13), (12, 14), (13, 14), (15, 16), (15, 17), (16, 17), (18, 19), (18, 20), (19, 20), (21, 22), (21, 23), (22, 23)]


H=Graph(24);
for (u,v) in Z:
    H.add_edge(u,v)
len(H.independent_set())


#Random generation of 3-covers of K_{4,4} which outputs the edges of the cover graph whenever no correspondence-colouring of the cover does exist.

from tqdm.notebook import (tqdm)
G = graphs.CompleteBipartiteGraph(4,4)
G.relabel()
G.show()

q = 3
n = G.order()
X=[]
counter=0
while counter<2000:
    H = Graph(q*n)

    # List of lists
    P = list(list(range(q*u, q*u+q)) for u in range(n))

    # Place a clique on each list
    for Lu in P:
        H.add_clique(Lu)


    # Place 'parallel' matchings along the spanning tree
    for (u, v) in [(0,4),(0,5),(0,6),(0,7),(1,4),(2,4),(3,4)]:
        for i in range(q):
            H.add_edge(q*u+i, q*v+i)


    for u in [1,2,3]:
        for v in [5,6,7]:
            p=Permutations(range(q)).random_element()
            for i in range(q):
                H.add_edge(q*u+i,q*v+p[i])
    X.append(len(H.independent_set()))
    counter+=1
    if len(H.independent_set())<8:
        H.edges()

