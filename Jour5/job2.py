def draw_rectangle(hauteur,largeur):

 c = '|'+'-'*(hauteur-2)+'|\n';
 print(c+c.replace(*'- ')*(largeur-2)+c)
 
draw_rectangle(10,3)