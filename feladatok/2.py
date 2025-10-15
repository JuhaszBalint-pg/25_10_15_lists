"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon,
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
"""

import random

gennums = []

for i in range (10):
    x = random.randint(1, 3)
    gennums.append(x)

print (gennums)
ui = int(input("Adj meg egy számot 1 és három között!\n"))

for i in range(gennums.count(ui)):
    gennums.remove(ui)
    
    """
    delnum = gennums.remove(ui)
    delnum += 1
    #print (gennums.count(delnum))
    if (gennums.count(delnum)) == 0:
        break
    else:
        continue
    """    
print (gennums)