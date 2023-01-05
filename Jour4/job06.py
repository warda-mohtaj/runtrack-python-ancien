L = [1, 2, 3, 4, 5]

for x,y in [(0,4)]:
    "inversement de l'ordre"
    L[x],L[y] = L[y],L[x]

print(L)