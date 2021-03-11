"""
Prologin: Entrainement 2003
Exercice: 11 - Anagrammes
https://prologin.org/train/2003/semifinal/anagrammes
"""
# Entrée
anagramme = []
anagrammes = {}
texte = input().split()

for mots in texte:
    mot = ''.join(sorted(mots))
    if mot in anagrammes:
        anagrammes[mot].append(mots)
    else:
        anagrammes[mot] = [mots]

for i in anagrammes:
    if len(anagrammes[i]) > 1:
        anagramme.append(i) 
        
print(len(anagramme))
print(anagrammes)
# Ne donne pas le bon résultat...