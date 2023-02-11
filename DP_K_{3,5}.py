#In this document, we verify that \chi_c(K_{3,5})=3 and \chi_c(K_{3,6})>3

#given the matchings x,y,z between L(u_i) and L(v), where the matching is presented by the neigbhours of L(v)=(1,2,3) resp. in L(u_i)
#output the 6 forbidden choices for the colouring of U, i.e. the colourings of U for which v cannot be coloured
def M(x,y,z):
    L=[]
    for c in Permutations([0,1,2]):
        L.append(tuple([x[c[0]],y[c[1]],z[c[2]]]))
    return L

#We first initialize the possible matchings between the L(v) and L(u) by ranging over all possibilities
#Here one matching is always taken to be the standard matching
d=[]
counter=0
P=Permutations([1,2,3])
for a in range(0,6):
    for b in range(0,6):
        d.append(M(P[0],P[a],P[b]))

︡
#we define a function that checks if all 3^3 tuples in {1,2,3}^3 appear in a list of tuples li 
#(i.e. we check if all 27 possible colourings of U lead to some vertex in V which cannot be coloured)
def all(li):
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if (i,j,k) not in li:
                    return false
                    break
    return true
︡
#We assume that the matching between v_1 and every u_i is the standard matching, and no two vertices v_i have the same matchings (that would be redundant)
#As such, for K_{3,5} there are still 4 other v_i for which we need to chooce the matchings
for c in Combinations(range(1,36),4):
    if all(d[0]+d[c[3]]+d[c[1]]+d[c[0]]+d[c[2]]):
        print(c)


︡

#we do the same for K_{3,6} and print only one bad combination
for c in Combinations(range(1,36),5):
    if all(d[0]+d[c[3]]+d[c[1]]+d[c[0]]+d[c[2]]+d[c[4]]):
        print(c)
        break
︡









