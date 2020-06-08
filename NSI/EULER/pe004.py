def pe004():
    """
    Retourne le plus grand palindrome obtenu par
    x × y, où x, y ont 3 chiffres.
    """

    def palindrome(nombre):
        "Retourne True si nombre est un palindrome"
        nombre_lu = str(nombre)
        return nombre_lu == nombre_lu[::-1]
     
    produit_palindrome = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            xy = x * y
            if palindrome(xy):
                produit_palindrome.append(xy)
    return max(produit_palindrome)

print(pe004())