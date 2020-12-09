def est_magique(n: int, grille: list) -> bool:
    """Une grille de taille n est-elle magique ?
    """
    somme = sum(grille[0]) # la somme de la première ligne
    # les autres lignes ?
    if any(sum(ligne) != somme
            for ligne in grille):
        return False
    # les autres colonnes ?
    if any(sum(grille[i][j] for i in range(n)) != somme
            for j in range(n)):
        return False
    # les diagonales ?
    if sum(grille[i][i] for i in range(n)) != somme:
        return False
    if sum(grille[i][-i-1] for i in range(n)) != somme:
        return False
    # tous les nombres de 1 à n² sont-ils présents ?
    # On enlève 1, pour un indice dans un tableau
    n_carré = n * n
    déjà_vu = [False for _ in range(n_carré)]
    for i in range(n):
        for j in range(n):
            if 0 < grille[i][j] <= n_carré:
                if déjà_vu[grille[i][j] - 1]:
                    return False
                déjà_vu[grille[i][j] - 1] = True
            else:
                return False
    # Alors tout est bon, le carré est magique
    return True

n = int(input())
grille = [list(map(int, input().split())) for _ in range(n)]
print('yes' if est_magique(n, grille) else 'no')
