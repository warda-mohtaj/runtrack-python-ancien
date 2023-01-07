def jcesar(msg="", clef=0): 
    alphabet="abcdefghijklmnopqrstuvwxyz" 
    chiffre="" 
  
    "prendre chaque lettre du mot et converti en minuscules"
    for c in msg.lower(): 
        "trouver la position de la lettre dans l'alphabet" 
        pos=alphabet.find(c) 
  
        "Gestion du chiffrement selon la présence ou pas de la lettre "
        chiffre+=alphabet[(pos+clef) % len(alphabet)] if pos != -1 else c 
    "for" 
    return chiffre 
"cesar()"
  
message="Hello World !!!" 
chiffre = jcesar(message, 6) 
dechiffre = jcesar(chiffre, -6) 
print (message, "=>", chiffre, "=>", dechiffre)