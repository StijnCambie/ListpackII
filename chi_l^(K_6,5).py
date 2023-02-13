
from tqdm.notebook import (tqdm)
from sage.graphs.independent_sets import IndependentSets

def gen_list_cover(G, L):

    n = G.order()
    assert(G.vertices(sort=True) == list(range(n)))

    H = Graph()
    for u in G.vertices(sort=False):
        H.add_clique([(u, c) for c in L[u]])

    for (u, v) in G.edges(sort=False, labels=False):
        for c in L[u] & L[v]:
            H.add_edge(((u, c), (v, c)))

    return H

T=Subsets(Subsets(5,3).list(),5).list()
T6=Subsets(Subsets(5,3).list(),6).list()

for p in T6:
    for q in T:
        G = graphs.CompleteBipartiteGraph(6,5)
        L=list(p)+list(q)
        H = gen_list_cover(G, L)
        if H.chromatic_number()>3:
            print(L)
