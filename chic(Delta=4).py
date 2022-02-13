#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list with all permutations of {1,2,3,4}
from itertools import permutations
L1 = list(permutations(range(1, 5)))

# intersection of two lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

#function that returns all derangements of a list
def derangements(L):
    return ( perm for perm in permutations(L)
             if all(p != L[indx] for indx, p in enumerate(perm)) )

#dictionary with the lists of all derangements of L1
dict1={};
for L in L1:
    dict1[L]=list(derangements(L))


# In[2]:


#Here we compute all bad combinations of possible colourings of the neighbours of the vertices u and v, 
#where wlog we assume that u_1 had colouring {1,2,3,4}

M=[];
S2=set();

for i in range(1,24):
    for j in range(0,23):
        for k in range(j+1,24):
            poss=False;
            for U in intersection(dict1[L1[0]],dict1[L1[i]]):
                for V in intersection(dict1[L1[j]],dict1[L1[k]]):
                    if U[0]!=V[0] and U[1]!=V[1] and U[2]!=V[2] and U[3]!=V[3]:
                        poss=True;
                        
            if poss==False:
                M.append([L1[i],L1[j],L1[k]]);
                S2.add(L1[i]);
M


# In[3]:


#We observe that any vertex for which 2 neighbours are already coloured, has at least 2 extensions 
#note that there does not necessarily an extension which is a derangement, in particular a K_4 which is precoloured in 2 vertices 
#cannot always be extended to a packing of the whole K_4
Lengths=[]
for h in range(0,23):
    for i in range(h+1,24):
        Lengths.append(len(intersection(dict1[L1[h]],dict1[L1[i]])))
min(Lengths)


# In[4]:


#Check that when u_1=v_1, one can avoid the bad configurations
S=[
#(1, 3, 4, 2),
#(1, 4, 2, 3),
#(2, 3, 1, 4),
 (2, 3, 4, 1),
 (2, 4, 1, 3),
# (2, 4, 3, 1),
# (3, 1, 2, 4),
 (3, 1, 4, 2),
# (3, 2, 4, 1),
## (3, 4, 2, 1),
 (4, 1, 2, 3),
# (4, 1, 3, 2),
# (4, 2, 1, 3),
## (4, 3, 1, 2)
]
for h in range(0,23):
    for i in range(h+1,24):
        if len(intersection(dict1[L1[h]],dict1[L1[i]]))-len(intersection(intersection(dict1[L1[h]],dict1[L1[i]]),S))==0:
            print(intersection(dict1[L1[h]],dict1[L1[i]]))


# In[5]:


S=[(1, 3, 2, 4),(3, 2, 1, 4),(4, 2, 3, 1),(1, 4, 3, 2)]
for h in range(0,23):
    for i in range(h+1,24):
        if len(intersection(dict1[L1[h]],dict1[L1[i]]))-len(intersection(intersection(dict1[L1[h]],dict1[L1[i]]),S))==0:
            print(intersection(dict1[L1[h]],dict1[L1[i]]))


# In[ ]:





# In[ ]:




