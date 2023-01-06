#%%
# Show that K_{3,3} is not fractionally 3-correspondence packable

from tqdm.notebook import (tqdm)
G = graphs.CompleteBipartiteGraph(3,3)
G.show()

q = 3
n = G.order()
H = Graph(q*n)

# List of lists
P = list(list(range(q*u, q*u+q)) for u in range(n))

# Place a clique on each list
for Lu in P:
    H.add_clique(Lu)
    
spanning_tree = set(next(G.spanning_trees()).edges(sort=False, labels=False))
remaining_edges = set(G.edges(sort=False, labels=False)) - spanning_tree

# Place 'parallel' matchings along the spanning tree
for (u, v) in spanning_tree:
    for i in range(q):
        H.add_edge(q*u+i, q*v+i)

print(f'spanning tree:   {spanning_tree}')
print(f'remaining edges: {remaining_edges}')

print('Generating covers...')
covers = {H.canonical_label(P).copy(immutable=True)}

reduce_by_P_iso_each_cover = True
reduce_by_iso_at_end = True

# For each remaining edge uv and all existing covers, put all possible matchings between L(u) and L(v)
for u, v in tqdm(remaining_edges):
    next_covers = set()
    for H in tqdm(covers, leave=False):
        for p in Permutations(range(q)):
            next_H = H.copy(immutable=False)
            for i in range(q):
                next_H.add_edge(q*u+i,q*v+p[i])
                
            if reduce_by_P_iso_each_cover:
                # store a canonical representative of the isomorphism class of next_H
                # under permutations that fix the lists
                next_covers.add(next_H.canonical_label(P).copy(immutable=True))
            else:
                # store next_H itself
                next_covers.add(next_H.copy(immutable=True))
        
        # continue iterating
        covers = next_covers
        
if reduce_by_iso_at_end:
    next_covers = covers
    
    pre_len = len(next_covers)
    covers_can = set()
    covers = set()
    for H in tqdm(next_covers):
        Hcan = H.canonical_label().copy(immutable=True)
        if Hcan not in covers_can:
            covers_can.add(Hcan)
            covers.add(H.copy(immutable=True))
    print(f'By isomorphism, reduced {pre_len} covers to {len(covers)}')
    
print('Computing properties...')
max_ir = 0
max_chif = 0
max_chi = 0

H_not_pack = []
H_not_frac = []
H_not_col = []


for H in tqdm(covers):
    chi  = H.chromatic_number()
    chif = q if chi  == q else H.fractional_chromatic_number(check_bipartite=False, check_components=False)
    ir   = q if chif == q else q*n/len(H.independent_set())
    
    if ir > max_ir:
        max_ir = ir
    if chif > max_chif:
        max_chif = chif
    if chi > max_chi:
        max_chi = chi

    if chi > q:
        H_not_pack.append(H)
    if chif > q:
        H_not_frac.append(H)
    if ir > q:
        H_not_col.append(H)

print(f'G is {"" if max_ir   == q else "not "}{q}-correspondence colorable')
print(f'G is {"" if max_chif == q else "not "}fractionally {q}-correspondence packable')
print(f'G is {"" if max_chi  == q else "not "}{q}-correspondence packable')
# %%
