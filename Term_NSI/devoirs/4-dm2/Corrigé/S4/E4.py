"""
Prologin: Entrainement 2003
Exercice: 4 - Initiales
https://prologin.org/train/2003/semifinal/initiales
"""
def initiales(texte):
  """Renvoie l'initiale de chaque mots de la phrase.
  >>> initiales('Rentre Avec tes pieds')
  RATP
  """ 
  lettre=""
  for i, c in enumerate(texte):
    if c!=" " and (i==0 or (i > 0 and texte[i-1] == " ")):
      lettre += c.upper()
  print(lettre)

# Test
import doctest
doctest.testmod()

# Entrées  
nb_lettre = int(input())
texte=input()

# Sortie
initiales(texte)