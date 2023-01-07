def Parcour(nb, h) :  
    print(f"Pour {nb} marches de {h}cm, il parcourt {nb*h*2*5*7/100.0:.2f}m par semaine .") 

nbrmarches = int(input("Combien de marches ? "))  
htrmarche = int(input("Hauteur d'une marche (cm) ? "))  
  
Parcour(nbrmarches, htrmarche)