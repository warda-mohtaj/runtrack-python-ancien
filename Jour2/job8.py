def nature (type, saison):

    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    if type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")

    if type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")

    if type == "légume" and saison == "été":
        print("artichaut, aubergine,navet")


nature ("fruits", "hiver")
nature ("fruits", "été")
nature ("légume", "hiver")
nature ("légume", "été")