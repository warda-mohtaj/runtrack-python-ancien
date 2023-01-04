chaine="abcdefghijklmnopqrstuvwxyz" * 10 
  
for pyramide in range(1, int((-1 + (1 + 8*len(chaine))**0.5) // 2) + 1): 
    print(chaine[:pyramide])  
    chaine=chaine[pyramide:]

"assez compliquer à comprendre quand meme "