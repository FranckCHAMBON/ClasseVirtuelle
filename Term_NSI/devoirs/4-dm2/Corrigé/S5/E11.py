nombre_caractères = int(input())

liste_mots = input().split(" ")

def sont_des_anagrammes(mot_1, mot_2):
    return sorted(mot_1) == sorted(mot_2)
        

dictionnaire_longueur = dict()
dictionnaire_anagramme = dict()

anagrammes = set()

for mot in liste_mots:
    longueur_mot = len(mot)
    if longueur_mot not in dictionnaire_longueur:
        set_mot = {mot}
        dictionnaire_longueur[longueur_mot] = set_mot
    else:
        dictionnaire_longueur[longueur_mot].add(mot)

for longueur_mot, set_mots in dictionnaire_longueur.items():
    if len(set_mots) == 1:
        pass
    else:
        liste_mots = list(set_mots)
        for mot_1 in liste_mots:
            for mot_2 in liste_mots:
                if mot_1 == mot_2:
                    continue
                elif sont_des_anagrammes(mot_1, mot_2):
                    if mot_1 not in dictionnaire_anagramme:
                        dictionnaire_anagramme[mot_1] = {mot_2}
                    else:
                        dictionnaire_anagramme[mot_1].add(mot_2)
                        if mot_2 not in dictionnaire_anagramme:
                            dictionnaire_anagramme[mot_2] = {mot_1}
                        else:
                            dictionnaire_anagramme[mot_2].add(mot_1)

def calcul_anagrammes():
    """
    Permet de calculer le nombre d'anagrammes dans la phrases et retourne leur nombre
    """
    déjà_vu = set()
    dictionnaire_anagramme_trié = sorted(dictionnaire_anagramme.items())
    for key, value in dictionnaire_anagramme_trié:
        for mot in value:
            if (mot, key) in déjà_vu:
                continue
            déjà_vu.add((key, mot))
    return len(déjà_vu)

print(calcul_anagrammes())