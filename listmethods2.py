honapok = ['január', 'február', 'március', 'április', 'május']
szamok = [1, 4, 6, 3, 7, 9, 20, 2]

#rendezés abc sorrendbe
reversed_sorted_honapok = sorted(honapok, reverse = True)
print (reversed_sorted_honapok)

honapok.sort() #nincsen visszaadási értéke
print (honapok)

#szamok novekő sorba rendezése
szamok.sort()
print (szamok)

sorted_szamok = sorted(szamok)
print (sorted_szamok)
reversed_sorted_szamok = sorted(szamok, reverse = True) #csökkenő sorrend
print (reversed_sorted_szamok)

print (szamok.index (20)) # megvizsgálja hanyas indexben szerepel az item
print (20 in szamok) # megvizsgálja szerepel e a listában

osszefog = honapok.extend(szamok)
print (osszefog)