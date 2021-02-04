from collections import deque


class File:
    def __init__(self):
        self.file = deque()
    
    def est_vide(self):
        return self.file == deque()

    def enfile(self, élément):
        self.file.append(élément)
    
    def défile(self):
        return self.file.popleft()


class Nœud:
    def __init__(self, gauche, élément, droite):
        self.gauche = gauche
        self.élément = élément
        self.droite = droite


class ABR:
    def __init__(self):
        self.racine = None
    
    def est_vide(self):
        return self.racine is None
    
    def ajoute(self, élément):
        "On ajoute sans dupliquer"
        if self.est_vide():
            self.racine = Nœud(ABR(), élément, ABR())
        elif élément < self.racine.élément:
            self.racine.gauche.ajoute(élément)
        elif élément > self.racine.élément:
            self.racine.droite.ajoute(élément)
        else:
            # en cas d'égalité, on ne fait rien ici
            pass
    
    def extrait_min(self):
        if self.est_vide():
            raise ValueError("ABR vide")
        if self.racine.gauche.est_vide():
            return self.racine.élément
        return self.racine.gauche.extrait_min()
    
    def est_présent(self, élément):
        if self.est_vide():
            return False
        elif élément < self.racine.élément:
            return self.racine.gauche.est_présent(élément)
        elif élément > self.racine.élément:
            return self.racine.droite.est_présent(élément)
        else:
            # Cas d'égalité
            return True

    def est_feuille(self):
        return self.racine.gauche.est_vide() and self.racine.droite.est_vide()
    
    def _repr(self, préfixe):
        if self.est_vide():
                return [préfixe[:-3] + '--']

        sortie = [préfixe[:-3] + '-- :' + str(self.racine.élément)]
        if not(self.est_feuille()):
            sortie.extend(self.racine.droite._repr(préfixe + '|   '))
            sortie.extend(self.racine.gauche._repr(préfixe + '    '))
        return sortie

    def __repr__(self):
        return "\n".join(self._repr('   '))

    def __str__(self):
        # Auteur : Franck CHAMBON
        code_dot = []
        ajout = code_dot.append
        ajout("digraph arbre {")
        sous_arbres = File()
        sous_arbres.enfile((1, self))
        while not sous_arbres.est_vide():
            id_sous_arbre, sous_arbre = sous_arbres.défile()
            if sous_arbre.est_vide():
                ajout(f'    {id_sous_arbre} [label="", shape=plaintext];')
            else:
                ajout(f'    "{id_sous_arbre}" [label="{sous_arbre.racine.élément}"];')
                id_gauche = 2*id_sous_arbre + 0
                id_droite = 2*id_sous_arbre + 1
                sous_arbres.enfile((id_gauche, sous_arbre.racine.gauche))
                sous_arbres.enfile((id_droite, sous_arbre.racine.droite))
                style_gauche = "[style=dashed, arrowhead=none]" if sous_arbre.racine.gauche.est_vide() else ""
                ajout(f'    "{id_sous_arbre}" -> "{id_gauche}"' + style_gauche +' ;')
                style_droite = "[style=dashed, arrowhead=none]" if sous_arbre.racine.droite.est_vide() else ""
                ajout(f'    "{id_sous_arbre}" -> "{id_droite}"' + style_droite +' ;')
        ajout('}')
        sortie = '\n'.join(code_dot)
        return sortie

    def affiche_en_ligne(self):
        """

        >>> exemple_abr = ABR()
        >>> for x in [21, 32, 11, 17, 24, 8, 16]: exemple_abr.ajoute(x)
        >>> exemple_abr.affiche_en_ligne()
        'https://dreampuf.github.io/GraphvizOnline/#digraph%20arbre%20%7B%0A%20%20%20%20%221%22%20%5Blabel%3D%2221%22%5D%3B%0A%20%20%20%20%221%22%20-%3E%20%222%22%20%3B%0A%20%20%20%20%221%22%20-%3E%20%223%22%20%3B%0A%20%20%20%20%222%22%20%5Blabel%3D%2211%22%5D%3B%0A%20%20%20%20%222%22%20-%3E%20%224%22%20%3B%0A%20%20%20%20%222%22%20-%3E%20%225%22%20%3B%0A%20%20%20%20%223%22%20%5Blabel%3D%2232%22%5D%3B%0A%20%20%20%20%223%22%20-%3E%20%226%22%20%3B%0A%20%20%20%20%223%22%20-%3E%20%227%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%20%224%22%20%5Blabel%3D%228%22%5D%3B%0A%20%20%20%20%224%22%20-%3E%20%228%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%20%224%22%20-%3E%20%229%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%20%225%22%20%5Blabel%3D%2217%22%5D%3B%0A%20%20%20%20%225%22%20-%3E%20%2210%22%20%3B%0A%20%20%20%20%225%22%20-%3E%20%2211%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%20%226%22%20%5Blabel%3D%2224%22%5D%3B%0A%20%20%20%20%226%22%20-%3E%20%2212%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%20%226%22%20-%3E%20%2213%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%207%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%208%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%209%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%20%2210%22%20%5Blabel%3D%2216%22%5D%3B%0A%20%20%20%20%2210%22%20-%3E%20%2220%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%20%2210%22%20-%3E%20%2221%22%5Bstyle%3Ddashed%2C%20arrowhead%3Dnone%5D%20%3B%0A%20%20%20%2011%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%2012%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%2013%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%2020%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%20%20%20%2021%20%5Blabel%3D%22%22%2C%20shape%3Dplaintext%5D%3B%0A%7D'

        """
        sortie = self.__str__()
        for x, y in [(" ", "%20"), ("\n", "%0A"), ("{", "%7B"), ('"', "%22"),
                     ("[", "%5B") ,("]", "%5D"), ("=", "%3D"), (";", "%3B"),
                     (">", "%3E"), (",", "%2C"), ("}", "%7D")]:
            sortie = sortie.replace(x, y)
        return "https://dreampuf.github.io/GraphvizOnline/#" + sortie



import doctest
doctest.testmod()

exemple_abr = ABR()
for x in [21, 32, 11, 17, 24, 8, 16]: exemple_abr.ajoute(x)
print(exemple_abr)