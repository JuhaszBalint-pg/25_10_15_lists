honapok = ['január', 'február','március', 'április', "május", "június"]

#a lista végéhez hozzáad egy elemet
honapok.append ("július")

#listához bizinyos indexxel hozzáad
honapok.insert (4, "augusztus")

#eltávolítja a legutolsó elemet
honapok.pop()
print (f"Utolsó hónap törölve: {honapok}")

torolt_honap = honapok.pop()
print (f"Az utolsó honap = {torolt_honap}")

#megadott indexű elemet töröl
torolt_honap = honapok.pop(0)
print (torolt_honap)
print (honapok)

torolt_honap = honapok.remove ("február") # a remove nem ad visszatérési értéket, míg a pop igen
print (torolt_honap)
print (honapok)
honapok.insert (0, "február")
print (honapok)

del honapok [1] #syntax error-ba fut a program ha megpróbálom kiprintelni
print (honapok)

#list kiürítése
honapok.clear()
print (honapok)
