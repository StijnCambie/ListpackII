#%%
# Load necessary definitions

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

def frac_colorable_with_demands(G, f):
    Is = [frozenset(S) for S in IndependentSets(G, maximal=True)]

    # Initialize LP for fractional coloring with local demands,
    # we want the total weight to be at most 1
    p = MixedIntegerLinearProgram(solver='PPL', maximization=False)

    # One nonnegative variable per maximal independent set
    w = p.new_variable(nonnegative=True)

    # The objective is the sum of weights of the independent sets
    p.set_objective(p.sum(w[S] for S in Is))

    # Such that each vertex gets total weight at least 1/f(v) for
    # the demand function f
    for u in G.vertices(sort=False):
        p.add_constraint(p.sum(w[S] for S in Is if u in S), min=f(u))

    obj = p.solve()
    return obj <= 1

def frac_deg_packable(G, L, H):
    Linv = dict()
    for u in G.vertices(sort=False):
        for x in L[u]:
            Linv[(u, x)] = u
    
    f = lambda x: 1/G.degree(Linv[x])
    return frac_colorable_with_demands(H, f)

#%%
# As a warm-up, show that the diamond is not fractionally degree-packable
G = graphs.DiamondGraph()
L = [{0,1}, {0,1,2}, {0,1,2}, {0,2}]
H = gen_list_cover(G, L)

print(frac_deg_packable(G, L, H)) # False

#%%
# Show that a K_4-necklace graph is not fractionally 3-list packable
G = graphs.DiamondGraph()
G = G.disjoint_union(graphs.DiamondGraph())
G.relabel()
G.add_edge((0,4))
G.add_edge((3,7))

r = 3
th = pi/3
G.set_pos({
    0: (    r*cos(5*th),     r*sin(5*th)),
    1: (    r*cos(0*th),     r*sin(0*th)),
    2: (1.7*r*cos(0*th), 1.7*r*sin(0*th)),
    3: (    r*cos(1*th),     r*sin(1*th)),
    7: (    r*cos(2*th),     r*sin(2*th)),
    5: (    r*cos(3*th),     r*sin(3*th)),
    6: (1.7*r*cos(3*th), 1.7*r*sin(3*th)),
    4: (    r*cos(4*th),     r*sin(4*th)),
})
G.show()

L = [{0,1,2}, {0,1,2}, {0,1,2}, {0,1,3}, {0,1,2}, {0,2,3}, {0,2,3}, {0,1,3}]
H = gen_list_cover(G, L)
print(L)
print(H.fractional_chromatic_number(check_bipartite=False, check_components=False)) # 34/11
# %%
H
# %%
