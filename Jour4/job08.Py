L= [ 8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

paire=0

for nbr in L:
    if nbr%2==0:
        paire= paire + nbr

print(paire)