︠49530a1f-7e01-4721-af94-481a5b9958b0s︠
#In this file, we prove that a bipartite graph on 16 vertices (with both bipartition classes of size 8) with min degree has either no perfect matchings, or at least 33.

#We first check regular graphs
#(equality is attained for exactly 3 of these)

gen = graphs.nauty_genbg("8 8 24:24 -d3 -D3")
L=list(gen)
len(L)

X=[]
for g in L:
    X.append(g.matching_polynomial()[0])
min(X)
︡24b11be6-a929-4603-95d4-6584c006339a︡{"stdout":"51\n"}︡{"stdout":"33\n"}︡{"done":true}
︠a15741c5-b4fb-426f-a2f3-ea1dd6c6e224︠
#Next, we check edge-minimal graphs with 25 up to 28 edges
#Edge-minimal; no edge can be removed without destroying the minimum degree 2 condition

#maxd1 and maxd2 are the intended maximum degrees of the two sides, where we choose maxd1 \ge maxd2
#we actually only assume that there are vertices of degree maxd1 and maxd2 on both sides, which we add later, and that the max degree is bounded by maxd1.
#The graphs are constructed in two steps

#edge-minimal case with size 25 up to 28
M=[]
for maxd1 in range(4,7):
    for maxd2 in range(4,maxd1+1):
        for size in range(21+maxd1,29):
            m=size-maxd1-maxd2;
            gen = graphs.nauty_genbg("7 7 "+str(m)+":"+str(m)+" -d2 -D"+str(maxd1));
            L=list(gen)
            len(L)


            for g in L:
                S=g.degree_sequence();
                S.reverse()
                if S[maxd1+maxd2]>2 and S[maxd1+maxd2-1]==2:
                    M.append(g)
            len(M)

︡a95cf301-d143-4de0-a6ed-46ac62f542ee︡{"stdout":"2194"}︡{"stdout":"\n651\n9650"}︡{"stdout":"\n4623"}︡{"stdout":"\n27451"}︡{"stdout":"\n7049"}︡{"stdout":"\n55884"}︡{"stdout":"\n7292"}︡{"stdout":"\n2427"}︡{"stdout":"\n8366\n12204"}︡{"stdout":"\n10882"}︡{"stdout":"\n43573"}︡{"stdout":"\n12650"}︡{"stdout":"\n352"}︡{"stdout":"\n12863\n2427"}︡{"stdout":"\n13452\n12204"}︡{"stdout":"\n14001"}︡{"stdout":"\n2427"}︡{"stdout":"\n14590\n12407"}︡{"stdout":"\n15231"}︡{"stdout":"\n352"}︡{"stdout":"\n15351\n2427"}︡{"stdout":"\n15455\n27\n15482\n352"}︡{"stdout":"\n15501\n"}︡{"done":true}
︠0f541a27-2f94-48aa-b77b-6c9b6600a635︠
#We construct the graphs and check that #p.m.'s is either 0 or at least 36 (for those)

SpecialCare=[]
X=[]
for g in M:
    for u in g.bipartition()[0]:
        if g.degree(u)==2:
            g.add_edge((u,14));
    for u in g.bipartition()[1]:
        if g.degree(u)==2:
            g.add_edge((u,15));
    if min(g.degree_sequence())==3:
        x=g.matching_polynomial()[0]
        if x>0:
            X.append(x)
        if x==0:
            SpecialCare.append(g)
min(X)
︡75e64627-8e00-46a2-88ce-387b3e6d44ce︡{"stdout":"36\n"}︡{"done":true}
︠723686c6-36a9-46b6-885e-ff1b4bbfa780︠
#Up to isomorphism, there are 6 graphs with 0 perfect matchings

SpecialCare2=[]
for g in SpecialCare:
    iso=False;
    for h in SpecialCare2:
        if g.is_isomorphic(h):
            iso=True
    if not iso:
        SpecialCare2.append(g)
len(SpecialCare2)
︡3baaa399-4bb0-410b-a5f7-d48df959fe4a︡{"stdout":"6\n"}︡{"done":true}
︠a90f5bbf-b0c5-40ad-86be-f5ceae72734a︠
#For those graphs, there is a restriction as 5 vertices in one side are connected with only 4 in the other side.
#It turns our that adding an edge, either results into at least 36 perfect matchings, or leaves the previous property.
#(if no edge of the above 20 is added, the number of pms was still 0)
#As such, all extensions which allow a p.m. have at least 36.

Scare=[]
Edges=[]
for g in SpecialCare2:
    Edges=[]
    for u in g.bipartition()[0]:
        for v in g.bipartition()[1]:
            if (u,v) not in g.edges(labels=False):
                h=g.copy()
                h.add_edge((u,v))
                if h.matching_polynomial()[0]<36 and h.matching_polynomial()[0]>0:
                    h.show()
                if h.matching_polynomial()[0]==0:
                    Scare.append(h)
                    Edges.append((u,v))
    #g.show()
    #Edges
    g.size()+len(Edges)
︡ba8874e8-d337-4ca8-914d-71daa714473c︡{"stdout":"44\n44"}︡{"stdout":"\n44\n44"}︡{"stdout":"\n44\n44"}︡{"stdout":"\n"}︡{"done":true}
︠681b75b6-5abb-4540-8da6-4057469ec401s︠

#Finally, we check the two edge-minimal graphs on 29 and 30 edges.
#Here one can check that there needs to be at least two disjoint edges spanned by the initial degree 3 vertices to have a perfect matching at the end
#No matter how this happends, at the end we have at least 36 perfect matchings

g=graphs.CompleteBipartiteGraph(5,3)*2
g.show()
g.add_edge((0,8))
g.add_edge((1,9))
g.matching_polynomial()[0]

g=graphs.CompleteBipartiteGraph(5,3)*2
g.delete_edge((0,5))
g.delete_edge((8,13))
g.add_edge((0,8))
g.show()
g.add_edge((1,9))
g.matching_polynomial()[0]

g=graphs.CompleteBipartiteGraph(5,3)*2
g.delete_edge((0,5))
g.delete_edge((8,13))
g.add_edge((0,8))
g.show()
g.add_edge((0,9))
g.add_edge((1,8))
g.matching_polynomial()[0]
︡af98e161-ef27-46e9-8937-97b0dfbe5e77︡{"file":{"filename":"/tmp/tmp23cejwe4/tmp_sii4dc27.svg","show":true,"text":null,"uuid":"885e6978-cab8-4e5a-9581-1aab1be8fc60"},"once":false}︡{"stdout":"36\n"}︡{"file":{"filename":"/tmp/tmp23cejwe4/tmp_8dgjcrzx.svg","show":true,"text":null,"uuid":"d674b888-eff0-4eb2-be9b-9ffbf0258447"},"once":false}︡{"stdout":"36\n"}︡{"file":{"filename":"/tmp/tmp23cejwe4/tmp_4afjxms4.svg","show":true,"text":null,"uuid":"129463a8-27eb-4c6d-9aa1-25453c4c162b"},"once":false}︡{"stdout":"36\n"}︡{"done":true}









