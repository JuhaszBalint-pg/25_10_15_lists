"""
1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást,
hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában!
Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""

colours = ['red', 'blue', 'green', 'cyan', 'white', 'black', 'blue']
urcolor = input("Please enter a colour!\n")

if urcolor in colours:
    print ("The entered colour is contained by the list!")
    print (f"Times when your colour appears in list: {colours.count(urcolor)}")
    print (", " .join(colours))

else: 
    print ("The enetered number is not contained by the list")
    print (", " .join(colours))