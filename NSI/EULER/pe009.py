def pe009(s=1000):
    """Solution au problème PE009
    trouver le triplet pythagoricien (a, b, c),
    a^2 + b^2 = c^2
    tel que a+b+c = s
    Complexité : O(s³)
    """
    # Rappel 0 < a < b < c < s
    for c in range(1, s):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    if a + b + c == s:
                        return a * b * c

assert pe009(12) == 60, "Le test avec 12 a échoué"

print(pe009())

