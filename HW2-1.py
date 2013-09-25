#HW2-1.py
#program by Valerie Lambert

"""
check for once sided stable matching with values.
lower is better
"""

import random

def randosituation(n):
    preferences = []
    for i in range(0,n):
        robotlist = []
        robotsfree = range(0, n)
        for j in range(0,n):
            p = random.randint(0,len(robotsfree)-1)
            robotlist.append(robotsfree[p])
            robotsfree.pop(p)
        preferences.append(robotlist)
    return preferences

def createpairing(bigarray):
    n = len(bigarray)
    S = []
    G = range(0, n)
    R = range(0, n)
    while len(G) > 0:
        g = G[random.randint(0, len(G)-1)]
        for r in bigarray[g]:
            print("g: " + str(g))
            print("G: " + str(G))
            print("r: " + str(r))
            print("R: " + str(R))
            print("S: " + str(S))
            if r in R:
                S.append((g, r))
                G.remove(g)
                R.remove(r)
                break
            else:
                for s in S:
                    if s[1] == r:
                        g2 = s[0]
                if g < g2:
                    S.remove((g2, r))
                    S.append((g, r))
                    G.append(g2)
                    G.remove(g)
                    break
                else:
                   pass 
    return S

def main():
    situation = randosituation(5)
    mylist = createpairing(situation)
    print(situation)
    print(mylist)

main()
