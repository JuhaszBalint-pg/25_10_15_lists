print ("A program kiírja a 3, 5 és mindkettővel osztható számokat")

dev3 = []
dev5 = []
devboth = []

for i in range (1, 101):
    if i%3==0:
        dev3.append(i)
    
    if i%5==0:
        dev5.append(i)

    
    
    if i%3==0 and i%5==0:
        devboth.append(i)

print(f"Mindkét számmal osztható számok: {devboth}")
print(f"3-al osztható számok: {dev3}")
print(f"5-el osztható számok: {dev5}")