"""
1.1 Feladat
A program tároljon egy listában színeket.
 Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában.
 A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""

colours = ['red', 'blue', 'green', 'cyan', 'white', 'black']
urcolor = input("Please enter a colour!\n")

if urcolor in colours:
    print ("The entered colour is contained by the list!")
    print (", " .join(colours))

else: 
    print ("The enetered number is not contained by the list")
    print (", " .join(colours))
