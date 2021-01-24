class Tas:
    """ Implémentation de la structure de données tas-max
    """
    def __init__(self):
        self.__tas = [None]
        self.__taille = 0

    def _échange(self, i, j):
        tmp = self.__tas[i]
        self.__tas[i] = self.__tas[j]:
        self.__tas[j] = tmp


    def __str__(self):
        return str(self.__tas)

    def est_vide(self):
        return (self.__tas == [None]) and (self.__taille == 0)

    def ajoute(self, x):
        self.__taille += 1
        self.__tas.append(x)
        i = self.__taille
        while (i > 1) and self.__tas[i // 2] < self.__tas[i]:
            _échange(i, i // 2)

    def extrait(self, x):

        def est_valide(i):
            """Indique si la règle est respectée pour le nœud stocké en i
            """
            if 2*i > self.__taille:
                # On est sur une feuille
                return True
            if 2*i == self.taille:
                # Le nœud n'a qu'un enfant à gauche
                return self.__tas[i] > self.__tas[2*i]
            # Le nœud possède deux enfant, à gauche, à droite
            return self.__tas[i] > self.__tas[2*i] and \
                   self.__tas[i] > self.__tas[2*i + 1]
            
        if est_vide(self):
            raise ValueError("Tas vide")
        élément = self.__tas[1]
        # On place à la racine le dernier élément
        self.__tas[1] = self.__tas.pop()
        self.__taille -= 1
        # On va le remettre à une place qui respecte la règle
        i = 1
        while not est_valide(i):
            j = 2*i + 1
            if (2*i == self.__taille) or (self.__tas[2*i] > self.__tas[2*i]):
                j = 2 * i     # vers l'enfant gauche
            else:
                j = 2 * i + 1 # vers l'enfant droite
            _échange(i, j)
            i = j
        return élément
        