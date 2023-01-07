def arrondir (notes):

  arrondies = []
  for note in notes:
    if note < 40:
      arrondies.append(note)

    elif note % 5 > 2:
      arrondies.append(note + (5 - note % 5))

    else:
      arrondies.append(note)
  return arrondies

notes = [38, 45, 82, 83.5, 84, 46.5]
notes_finales = arrondir(notes)

print(notes_finales)