honapok = ['január', 'február','március', 'április', "május", "június"]

print(type(honapok))

print(len(honapok))
#elemek mennyiségének "hoszzának" kiiratása

#a 0 index az első elem
print(honapok [0])
print(honapok [1])
print(honapok [2])
print(type(honapok[2]))

# minusz első elem, az utolsó elem, a minusz a fordított sorrendet mutatja
print (f"Az utolsó elem a listában: {honapok [-1]}")

# a lista periodusát irja ki, utolsó indexet nem veszi bele
print (honapok[1 : 3])
print (type(honapok[1:3]))

# a lista 3. eleméig írja ki
print (honapok [:3])

# a lista 2. elemétől írja ki
print (honapok [2:])

#str-é összefűzés
print (", " .join(honapok))

#lista bejárása for in range ciklussal
for i in range(len(honapok)):
    print (honapok[i])

#lista bejárása for - items ciklussal
print ("\nHónapok:\n")
for honap in (honapok):
    print (honap)

index = 0
for honap in honapok:
    print (index , honap)
    index += 1