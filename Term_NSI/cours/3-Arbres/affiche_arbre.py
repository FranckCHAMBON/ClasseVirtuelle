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


def affiche(arbre, titre=None):
    code_dot = []
    ajout = code_dot.append
    ajout("digraph arbre {")
    if titre:
        ajout('label = "{titre}" ;')
    nœuds = File()
    nœuds.enfile((1, arbre))
    while not nœuds.est_vide():
        id_nœud, nœud = nœuds.défile()
        if nœud is not None:
            ajout(f'    "{id_nœud}" [label="{nœud.élément}"];')

            id_gauche = 2*id_nœud + 0
            id_droite = 2*id_nœud + 1
            nœuds.enfile((id_gauche, nœud.gauche))
            nœuds.enfile((id_droite, nœud.droite))
            
            style_gauche = "[style=dashed, arrowhead=none]" if nœud.gauche is None else ""
            ajout(f'    "{id_nœud}" -> "{id_gauche}"' + style_gauche +' ;')
            style_droite = "[style=dashed, arrowhead=none]" if nœud.droite is None else ""
            ajout(f'    "{id_nœud}" -> "{id_droite}"' + style_droite +' ;')
            
        else:
            ajout(f'    {id_nœud} [label="", shape=plaintext];')
    
    ajout('}')
    return '\n'.join(code_dot)


def _repr(nœud, préfixe):
    if nœud is None:
            return [préfixe[:-3] + '--']

    code_dot = [préfixe[:-3] + '-- :' + str(nœud.élément)]
    if (nœud.gauche) and (nœud.droite):
        code_dot.extend(_repr(nœud.gauche, préfixe + '|   '))
        code_dot.extend(_repr(nœud.droite, préfixe + '    '))
    return code_dot

def repr(arbre):
    return "\n".join(_repr(arbre, '   '))

six_1 = Nœud(None, "6", None)
cinq_1 = Nœud(None, "5", None)
produit_1 = Nœud(six_1, "×", cinq_1)

trois_1 = Nœud(None, "3", None)

sept_1 = Nœud(None, "7", None)
six_2 = Nœud(None, "6", None)
somme_1 = Nœud(sept_1, "+", six_2)

somme_2 = Nœud(trois_1, "+", somme_1)
expr_A = Nœud(produit_1, "-", somme_2)


print(repr(expr_A))
