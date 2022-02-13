#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Creates the 4-fold cover graph of the K_4 and initialises the matchings in a tree 
K4=graphs.CompleteGraph(4)
H=4*K4
for i in range(0,12):
    H.add_edge(i,i+4)


# In[2]:

#we generate all possible matchings on the remaining 3 edges and 
#check that the correspondence-cover has always chromatic number 4
for p1 in Permutations(range(8,12)):
    for p2 in Permutations(range(12,16)):
        for p3 in Permutations(range(12,16)):
            G=H.copy()
            for i in range(0,4):
                G.add_edge(i ,p1[i]);
                G.add_edge(i ,p2[i]);    
                G.add_edge(i+4 ,p3[i]);
            if G.chromatic_number()!=4:
                print(G)







