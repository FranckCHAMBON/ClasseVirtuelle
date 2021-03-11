"""
Prologin:  Entraînement  2003
Exercice: 11 - Anagrammes
https://prologin.org/train/2003/semifinal/anagrammes
"""
def anagrammes(phrase, nb_anagrammes: int):
    """ cherche le nombre d'anagrammes qui existe dans la phrase
    """
    phrase1 = []
    phrase2 = []
    phrase.sort()
    phrase = sorted(phrase, key= len)
    for x in range(len(phrase) - 1):
        if len(phrase[x]) == len(phrase[x + 1]):
            if phrase[x] != phrase[x + 1]:
                for y in phrase[x]:
                    phrase1.append(y)
                phrase1.sort()
                for y in phrase[x + 1]:
                    phrase2.append(y)
                phrase2.sort()
                if phrase1 == phrase2: 
                    nb_anagrammes += 1           
    return nb_anagrammes


nb_caractère = int(input())
phrase = input().split()
nb_anagrammes = 0
print(anagrammes(phrase, nb_anagrammes))
"je voie pas où est le problème"
